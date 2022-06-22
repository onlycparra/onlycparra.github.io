PUBLIC = public
ORG = org
ALL_ORGS = $(sort $(shell find $(ORG) -type f -name '*.org'))
NO_PAGES = org/template.org org/config.org
PAGES = $(patsubst %.org,%.html,$(filter-out $(NO_PAGES),$(ALL_ORGS)))
DEST_ORGS = $(patsubst $(ORG)/%,$(PUBLIC)/%,$(ALL_ORGS))

.PHONY: all clean

all: $(PAGES) $(PUBLIC)

%.html: %.org
	emacs $< --batch -f org-html-export-to-html --kill

$(PUBLIC):
	mkdir -p $(PUBLIC)
	cp -rT $(ORG) $(PUBLIC)
	rm -f $(DEST_ORGS)

clean:
	rm -rf $(PUBLIC)
	rm -f $(PAGES)

echo:
	@echo $(ALL_ORGS) | tr ' ' '\n'
	@echo
	@echo $(NO_PAGES) | tr ' ' '\n'
	@echo
	@echo $(PAGES) | tr ' ' '\n'
	@echo
	@echo $(DEST_ORGS) | tr ' ' '\n'
