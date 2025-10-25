
#include <linux/cpu.h>

#define CPU_CONTROL_DIR "cpu_control"

static struct kobject *cpu_control_kobj;

static bool cpu_valid(unsigned int cpu)
{
	return cpu < num_possible_cpus();
}

static void log_cpu_state(unsigned int cpu)
{
	if (cpu_online(cpu)) {
		pr_info("CPU %u: ONLINE\n", cpu);
	} else {
		pr_info("CPU %u: OFFLINE\n", cpu);
	}
}

static ssize_t enable_store(struct kobject *kobj,
			    struct kobj_attribute *attr,
			    const char *buf,
			    size_t count)
{
	unsigned int cpu;
	int ret;

	ret = kstrtouint(buf, 10, &cpu);
	if (ret) {
		pr_err("Invalid CPU ID: %s\n", buf);
		return ret;
	}

	if (!cpu_valid(cpu)) {
		pr_err("CPU %u is not valid (max: %u)\n",
		       cpu, num_possible_cpus() - 1);
		return -EINVAL;
	}

	if (cpu_online(cpu)) {
		pr_info("CPU %u already enabled.\n", cpu);
		return count;
	}

	ret = add_cpu(cpu);
	if (ret) {
		pr_err("Failed to enable CPU %u: %d\n", cpu, ret);
		return ret;
	}

	pr_info("CPU %u enabled successfully.\n", cpu);
	log_cpu_state(cpu);

	return count;
}

static ssize_t disable_store(struct kobject *kobj,
			     struct kobj_attribute *attr,
			     const char *buf,
			     size_t count)
{
	unsigned int cpu;
	int ret;

	ret = kstrtouint(buf, 10, &cpu);
	if (ret) {
		pr_err("Invalid CPU ID: %s\n", buf);
		return ret;
	}

	if (!cpu_valid(cpu)) {
		pr_err("CPU %u is not valid (max: %u)\n", cpu,
		       num_possible_cpus() - 1);
		return -EINVAL;
	}

	if (!cpu_online(cpu)) {
		pr_info("CPU %u already disabled.\n", cpu);
		return count;
	}

	ret = remove_cpu(cpu);
	if (ret) {
		pr_err("Failed to disable CPU %u: %d\n", cpu, ret);
		return ret;
	}

	pr_info("CPU %u disabled successfully.\n", cpu);
	log_cpu_state(cpu);

	return count;
}

static ssize_t toggle_store(struct kobject *kobj,
			    struct kobj_attribute *attr,
			    const char *buf,
			    size_t count)
{
	unsigned int cpu;
	int ret;

	ret = kstrtouint(buf, 10, &cpu);
	if (ret) {
		pr_err("Invalid CPU ID: %s\n", buf);
		return ret;
	}

	if (!cpu_valid(cpu)) {
		pr_err("CPU %u is not valid (max: %u)\n",
		       cpu, num_possible_cpus() - 1);
		return -EINVAL;
	}

	if (cpu_online(cpu)) {
		ret = remove_cpu(cpu);
		if (ret) {
			pr_err("Failed to disable CPU %u during toggle: %d\n",
			       cpu, ret);
			return ret;
		}
		pr_info("CPU %u toggled OFF.\n", cpu);
	} else {
		ret = add_cpu(cpu);
		if (ret) {
			pr_err("Failed to enable CPU %u during toggle: %d\n",
			       cpu, ret);
			return ret;
		}
		pr_info("CPU %u toggled ON.\n", cpu);
	}

	log_cpu_state(cpu);
	return count;
}

static struct kobj_attribute enable_attr = __ATTR_WO(enable);
static struct kobj_attribute disable_attr = __ATTR_WO(disable);
static struct kobj_attribute toggle_attr = __ATTR_WO(toggle);

static struct attribute *attrs[] = {
	&enable_attr.attr,
	&disable_attr.attr,
	&toggle_attr.attr,
	NULL,
};

static struct attribute_group attr_group = {
	.attrs = attrs,
};

static int __init cpu_control_init(void)
{
	int ret;

	pr_info("CPU Control Module loaded.\n");

	cpu_control_kobj = kobject_create_and_add(CPU_CONTROL_DIR, kernel_kobj);
	if (!cpu_control_kobj) {
		pr_err("Failed to create kobject.\n");
		return -ENOMEM;
	}

	ret = sysfs_create_group(cpu_control_kobj, &attr_group);
	if (ret) {
		pr_err("Failed to create sysfs group: %d\n", ret);
		kobject_put(cpu_control_kobj);
		return ret;
	}

	pr_info("CPU control interface created at /sys/kernel/%s\n",
		CPU_CONTROL_DIR);
	pr_info("Usage: echo <cpu_id> > /sys/kernel/%s/enable|disable|toggle\n",
		CPU_CONTROL_DIR);

	return 0;
}

static void __exit cpu_control_exit(void)
{
	if (cpu_control_kobj) {
		sysfs_remove_group(cpu_control_kobj, &attr_group);
		kobject_put(cpu_control_kobj);
		pr_info("CPU Control Module unloaded.\n");
	}
}

module_init(cpu_control_init);
module_exit(cpu_control_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Konstantin Semichastnov");
MODULE_DESCRIPTION("Dynamic CPU core enable/disable via sysfs");
MODULE_VERSION("1.0");
