PUBLIC = docs
ORG = org
NOT_ORGS = $(sort $(shell find $(ORG) -type f -not -name '*.org' -not -name '*~'))
DEST_NOT_ORGS = $(patsubst $(ORG)/%,$(PUBLIC)/%,$(NOT_ORGS))
ALL_ORGS = $(sort $(shell find $(ORG) -type f -name '*.org'))
NO_PAGES = org/template.org org/config.org org/nav.org
PAGES = $(patsubst %.org,%.html,$(filter-out $(NO_PAGES),$(ALL_ORGS)))
DEST_ORGS = $(patsubst $(ORG)/%,$(PUBLIC)/%,$(ALL_ORGS))

.PHONY: all clean echo

all: $(PAGES) $(DEST_NOT_ORGS)

%.html: %.org
	@echo "Exporting: $@"
	@emacs $< --batch -f org-html-export-to-html --kill 2>/dev/null
	@mkdir -p $(dir $(patsubst $(ORG)/%,$(PUBLIC)/%,$@))
	cp -f $@ $(patsubst $(ORG)/%,$(PUBLIC)/%,$@)

$(PUBLIC)/%: $(ORG)/%
	@mkdir -p $(dir $(patsubst $(ORG)/%,$(PUBLIC)/%,$@))
	cp -f $< $(patsubst $(ORG)/%,$(PUBLIC)/%,$@)

clean:
	rm -rf $(PUBLIC)
	@rm -f $(PAGES)

echo:
	@echo $(ALL_ORGS) | tr ' ' '\n'
	@echo
	@echo $(NO_PAGES) | tr ' ' '\n'
	@echo
	@echo $(PAGES) | tr ' ' '\n'
	@echo
	@echo $(DEST_ORGS) | tr ' ' '\n'
