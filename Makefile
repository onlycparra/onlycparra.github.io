PUBLIC := docs
ORG := org
BUILD_LOG := build.log
# any file with this string in its path, will be omited.
OMIT_STR := __

# explicit list of org files that don't have to be converted to html
NO_PAGES := 

# exclude from find
NO_FIND := -not -name '*~' -not -wholename '*$(OMIT_STR)*' -not -wholename '*/.*'
# all org files
ALL_ORGS := $(sort $(shell find -L $(ORG) -type f -name '*.org' $(NO_FIND)))
# all html files generated from org files
PAGES := $(patsubst %.org,%.html,$(filter-out $(NO_PAGES),$(ALL_ORGS)))

# all assets that are not .org files
ASSETS := $(sort $(shell find -L $(ORG) -type f -not -name '*.org' $(NO_FIND)))
ASSETS := $(filter-out $(PAGES),$(ASSETS))
# where to put not-org assets in the target directory.
DEST_ASSETS := $(patsubst $(ORG)/%,$(PUBLIC)/%,$(ASSETS))

SHELL := /bin/bash
ERROR_COLOR := \033[31m
RESET_COLOR := \033[39m

.PHONY: all everything clean-log clean echo show-log

all: clean-log
	@(\
		set -e ;\
		set -o pipefail ;\
		$(MAKE) --no-print-directory build-all |\
			tee -a $(BUILD_LOG) 2>>$(BUILD_LOG) ||\
				( \
					echo -en "\n$(ERROR_COLOR)Error while building targets. " ;\
					echo -e "Showing tail of $(BUILD_LOG):$(RESET_COLOR)" ;\
					$(MAKE) --no-print-directory show-log \
				) ;\
		set +o pipefail ;\
	)

build-all: $(PAGES) $(DEST_ASSETS)

%.html: %.org
	@echo  "$<  --->  $(patsubst $(ORG)/%,$(PUBLIC)/%,$@)"
	@emacs --batch -f package-initialize $< \
		--eval "(progn (setq org-html-htmlize-output-type 'css) (org-html-export-to-html))" \
		--kill  >>$(BUILD_LOG) 2>>$(BUILD_LOG)
	@mkdir -p $(dir $(patsubst $(ORG)/%,$(PUBLIC)/%,$@))
	@cp -f $@ $(patsubst $(ORG)/%,$(PUBLIC)/%,$@)

$(PUBLIC)/%: $(ORG)/%
	@mkdir -p $(dir $(patsubst $(ORG)/%,$(PUBLIC)/%,$@))
	@echo "$<  --->  $(patsubst $(ORG)/%,$(PUBLIC)/%,$@)"
	@cp -f $< $(patsubst $(ORG)/%,$(PUBLIC)/%,$@)

clean:
	rm -f $(BUILD_LOG)
	rm -rf $(PUBLIC)
	@echo "removing page files '$(ORG)/**.html'"
	@rm -f $(PAGES)

show-log:
	@tail -n 30 $(BUILD_LOG)

clean-log:
	@rm -f $(BUILD_LOG)

echo:
	@echo -e "Any directory or file containing '$(OMIT_STR)' in its path is ignored.\n"

	@echo "All org-files in the source directory:"
	@echo $(ALL_ORGS) | tr ' ' '\n'

	@echo -e "\nExplicit list of org-files that will not be converted to html:"
	@echo $(NO_PAGES) | tr ' ' '\n'

	@echo -e "\nPages to generate:"
	@echo $(PAGES) | tr ' ' '\n'

	@echo -e "\nOther assets in source directory to simply copy:"
	@echo $(ASSETS) | tr ' ' '\n'

continuous-build:
	@echo "Waiting for changes in '$(ORG)/'"
	@echo "[Ctrl-C] to exit."
	@find -L $(ORG) -type f -not -name '*~' -not -wholename '*/.*' -not -name '*.html' | entr -pc make --no-print-directory all

serve-website:
	@(\
		cd $(PUBLIC) ;\
		python3 -m http.server ;\
	)
