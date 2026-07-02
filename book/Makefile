CHAPTERS := $(sort $(wildcard chapters/*.md))
PANDOC := pandoc
PANDOC_FLAGS := --from markdown+tex_math_dollars+smart \
                --bibliography bibliography.bib \
                --citeproc \
                --metadata-file metadata.yaml

.PHONY: all html pdf epub clean

all: html

html: audio_signal_processing.html

pdf: audio_signal_processing.pdf

epub: audio_signal_processing.epub

audio_signal_processing.html: $(CHAPTERS) metadata.yaml bibliography.bib
	$(PANDOC) $(PANDOC_FLAGS) $(CHAPTERS) -o $@

audio_signal_processing.pdf: $(CHAPTERS) metadata.yaml bibliography.bib
	$(PANDOC) $(PANDOC_FLAGS) $(CHAPTERS) -o $@

audio_signal_processing.epub: $(CHAPTERS) metadata.yaml bibliography.bib
	$(PANDOC) $(PANDOC_FLAGS) $(CHAPTERS) -o $@

clean:
	rm -f audio_signal_processing.html audio_signal_processing.pdf audio_signal_processing.epub
