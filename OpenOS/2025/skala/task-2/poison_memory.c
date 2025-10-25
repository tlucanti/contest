
#include <linux/module.h>
#include <linux/mm.h>

#ifndef POISON_PERCENTAGE
#define POISON_PERCENTAGE 10
#endif
#if POISON_PERCENTAGE < 0 || POISON_PERCENTAGE > 100
#error "POISON_PERCENTAGE must be between 0 and 100"
#endif

static int poison_page(unsigned long pfn)
{
	int ret = 0;

	if (!pfn_valid(pfn)) {
		pr_warn("Invalid PFN: %lu\n", pfn);
		return EINVAL;
	}

	/*
	 * tell linux to offline page to safely inject poison flag to it
	 */
	ret = soft_offline_page(pfn, 0);
	if (ret) {
		pr_warn("Failed to set page offline at PFN %lu\n", pfn);
		return ret;
	}

	SetPageHWPoison(pfn_to_page(pfn));

	pr_info("Poisoned page at PFN %lu successfully.\n", pfn);

	return 0;
}

static int __init hwpoison_init(void)
{
	unsigned long total_pages = totalram_pages();
	unsigned long pages_to_poison = (total_pages * POISON_PERCENTAGE) / 100;
	unsigned long poisoned = 0;
	pages_to_poison = 1;

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
