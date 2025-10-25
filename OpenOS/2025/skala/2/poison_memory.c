#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/mm.h>
#include <linux/slab.h>
#include <linux/uaccess.h>
#include <asm/page.h>

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/mm.h>
#include <linux/slab.h>
#include <linux/pagemap.h>
#include <linux/vmalloc.h>
#include <asm/page.h>
#include <asm/pgtable.h>

#include <linux/page-flags.h>

#ifndef POISON_PERCENTAGE
#define POISON_PERCENTAGE 10
#endif
#if POISON_PERCENTAGE < 0 || POISON_PERCENTAGE > 100
#error "POISON_PERCENTAGE must be between 0 and 100"
#endif

#ifndef POISON_FREE_ONLY
#define POISON_FREE_ONLY true
#endif

static int poison_page(unsigned long pfn)
{
	int ret = 0;

	if (!pfn_valid(pfn)) {
		pr_warn("Invalid PFN: %lu\n", pfn);
		return EINVAL;
	}

	if (POISON_FREE_ONLY) {
		/*
		 * only poison free pages, to prevent killing accessing
		 * this page processes
		*/
		struct page *page = pfn_to_page(pfn);

		if (PageBuddy(page) && PageSlab(page) && !PageReserved(page)) {
			pr_warn("Skipped page in use at PFN %lu\n", pfn);
			return EPERM;
		}
	}

	SetPageHWPoison(pfn_to_page(pfn));
	if (ret) {
		pr_warn("Failed to poison page at PFN %lu (error %d)\n",
			pfn, ret);
		return EINVAL;
	}

	pr_info("Poisoned page at PFN %lu successfully.\n", pfn);

	return 0;
}

static int __init hwpoison_init(void)
{
	unsigned long total_pages = totalram_pages();
	unsigned long pages_to_poison = (total_pages * POISON_PERCENTAGE) / 100;
	unsigned long poisoned = 0;

	pr_info("Memory Poison Module loaded (poisoning %d%% of RAM).\n",
		POISON_PERCENTAGE);
	pr_info("Total physical pages: %lu\n", total_pages);
	pr_info("Targeting %lu pages to poison\n", pages_to_poison);


	for (unsigned long pfn = 0; pfn < total_pages; pfn++) {
		if (poison_page(pfn)) {
			continue;
		}

		poisoned++;
		if (poisoned >= pages_to_poison) {
			break;
		}
	}

	if (poisoned >= pages_to_poison) {
		pr_info("Successfully poisoned %lu pages.\n", poisoned);
	} else {
		pr_err("Poisoned only %lu pages, out of target %lu.\n",
		        poisoned, pages_to_poison);
	}

	return 0;
}

static void __exit hwpoison_exit(void)
{
	pr_info("Memory Poison Module unloaded\n");
}

module_init(hwpoison_init);
module_exit(hwpoison_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Konstantin Semichastnov");
MODULE_DESCRIPTION("Module to poison memory via HWPOISON.");
MODULE_VERSION("1.0");
