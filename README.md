# Auto-GPT-Plugin-Template
A Plugin for [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) that adds YouTube support.

## Features
- [x] Download YouTube videos
- [x] Download YouTube audio
- [x] Search YouTube
- [x] Download YouTube Subtitles (Transcription)
- [x] Fetch comments of a YouTube video
- [x] Get video information

### Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository, or download the repository as a zip file.
  
   ![Download Zip](https://i.imgur.com/dvGqLMX.png)

2. **Install the plugin's dependencies:**
   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   If you cloned the repository, compress the plugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPT_YouTube,example-plugin1,example-plugin2
   ```

   If the plugin is not allowlisted, you will be warned before it's loaded.

6. **Configure the plugin:**
   Add the plugin's configuration to the `.env` file:

   ``` shell
   ################################################################################
   ### YOUTUBE
   ################################################################################

   YOUTUBE_API_KEY=your-api-key
   ```
