# Additional samd21 build rules

# Setup the toolchain
CROSS_PREFIX=arm-none-eabi-

dirs-y += src/samd21 src/generic
dirs-y += lib/samd21/samd21a/gcc/gcc/

CFLAGS += -mthumb -mcpu=cortex-m0plus
CFLAGS += -Ilib/cmsis-core -Ilib/samd21/samd21a/include
CFLAGS += -D__SAMD21G18A__

CFLAGS_klipper.elf += -Llib/samd21/samd21a/gcc/gcc/
CFLAGS_klipper.elf += -T lib/samd21/samd21a/gcc/gcc/samd21g18a_flash.ld
CFLAGS_klipper.elf += --specs=nano.specs --specs=nosys.specs

# Add source files
src-y += samd21/main.c samd21/timer.c samd21/clock.c samd21/gpio.c
src-y += generic/crc16_ccitt.c generic/alloc.c
src-y += generic/armcm_irq.c generic/timer_irq.c
#src-y += ../lib/samd21/samd21a/gcc/system_samd21.c
src-y += ../lib/samd21/samd21a/gcc/gcc/startup_samd21.c
src-$(CONFIG_SERIAL) += samd21/serial.c generic/serial_irq.c

# Build the additional hex output file
target-y += $(OUT)klipper.bin

$(OUT)klipper.bin: $(OUT)klipper.elf
	@echo "  Creating hex file $@"
	$(Q)$(OBJCOPY) -O binary $< $@

target-y += $(OUT)klipper.elf.hex

$(OUT)klipper.elf.hex: $(OUT)klipper.elf
	@echo "  Creating hex file $@"
	$(Q)$(OBJCOPY) -j .text -j .relocate -O ihex $< $@

flash: $(OUT)klipper.bin
	@echo "  Flashing $^ to $(FLASH_DEVICE) via bossac"
	$(Q)stty -F "$(FLASH_DEVICE)" 1200
	$(Q)bossac -i -p "$(FLASH_DEVICE:/dev/%=%)" -R -e -w -v -b $(OUT)klipper.bin
