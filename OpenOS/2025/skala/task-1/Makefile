
obj-m += cpu_control.o
KDIR ?= /lib/modules/$(shell uname -r)/build

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
	rm -f *.ko *.o *.order *.symvers *.mod.c *.mod .*.cmd

install:
	sudo insmod cpu_control.ko
	sudo chmod 666 /sys/kernel/cpu_control/enable
	sudo chmod 666 /sys/kernel/cpu_control/disable
	sudo chmod 666 /sys/kernel/cpu_control/toggle

uninstall:
	sudo rmmod cpu_control
