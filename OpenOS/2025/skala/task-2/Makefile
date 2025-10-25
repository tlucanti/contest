
obj-m += poison_memory.o
KDIR ?= /lib/modules/$(shell uname -r)/build

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
	rm -f *.ko *.o *.order *.symvers *.mod.c *.mod .*.cmd

install:
	sudo insmod poison_memory.ko

uninstall:
	sudo rmmod poison_memory
