SOURCES:= include/ualberta include/common
OUTPUTS:=$(patsubst %.xml, include/%, %(SOURCES))


all: $(SOURCES)
include/%:message_definitions/%.xml
	python udenver_generate.py $<
clean:
	rm -rf $(SOURCES)
