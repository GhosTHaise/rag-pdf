from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor
)

from llama_index.core.node_parser import SentenceSplitter

text_splitter = SentenceSplitter(
    separator=" ",chunk_size=1024, chunk_overlap=128
)

title_extractor = TitleExtractor(llm=llm_transformations, nodes=5)
qa_extractor = QuestionsAnsweredExtractor(llm=llm_transformations, questions=3)

from llama_index.core.ingestion import IngestionPipeline

pipeline.load("./pipeline_storage")

pipeline = IngestionPipeline(
    transformations=[
        text_splitter,
        title_extractor,
        qa_extractor
    ]
)

pipeline.persist("./pipeline_storage")

nodes = pipeline.run(
    documents=docs,
    in_place=True,
    show_progress=True
)