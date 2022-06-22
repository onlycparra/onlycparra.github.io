PUBLIC = public
ASSETS = assets
ORG = org
PER_DIR = $(wildcard $(ORG)/personal/*.org)
RES_DIR = $(wildcard $(ORG)/research/*.org)
PRO_DIR = $(wildcard $(ORG)/professional/*.org)
ORG_FILES = $(ORG)/index.org $(PER_DIR) $(RES_DIR) $(PRO_DIR)
HTML_FILES = $(patsubst $(ORG)/%.org,$(PUBLIC)/%.html,$(ORG_FILES))

.PHONY: all clean install-doc

all: install-doc

$(PUBLIC):
	mkdir -p $(PUBLIC)

install-doc: $(PUBLIC) $(HTML_FILES) $(PUBLIC)/$(ASSETS)

$(PUBLIC)/%.html: $(ORG)/%.html $(PUBLIC)
	install -Dvm 644 -T $< $@ && rm $<

$(ORG)/%.html: $(ORG)/%.org
	emacs $< --batch -f org-html-export-to-html --kill

$(PUBLIC)/$(ASSETS): $(ORG)/$(ASSETS) $(PUBLIC)
	cp -r $< $@

clean:
	rm -rf $(PUBLIC)
	rm -f $(patsubst %.org,%.html,$(ORG_FILES))
