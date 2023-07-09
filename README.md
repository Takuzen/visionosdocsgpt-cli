# emb-vos-doc

This is made to be a tool for helping visionOS developers build great application with the aid of ChatGPT which has the knowledge of the latest Apple's visionOS documentation.

## Initailization

1. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

2. Create .env file, and specify your OpenAI key as follows:

    ```
    OPENAI_API_KEY=...
    PINECONE_API_KEY=...
    PINECONE_ENVIRONMENT=...
    ```

3. Run `scrapying.py` for generating CSV file like:

    ```
    $ python scraping.py
    ```

4. Run `main.py`:

    ```
    $ python main.py
    ```

Then you should get reply (output) like this:

 Q: What is Apple visionOS? <br/>
 A: Apple visionOS is the operating system that powers Vision Pro. It is used to build immersive apps and games for spatial computing.
    
