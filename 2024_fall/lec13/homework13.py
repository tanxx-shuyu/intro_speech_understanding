import bs4
from gtts import gTTS


def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com (npr.org) webpage.

    @params:
        text (string): The HTML/text of a webpage.

    @returns:
        stories (list of tuples of strings):
            A list of news stories in the webpage.
            Each story is a tuple of (title, teaser), where the title and teaser
            are both strings. If the story has no teaser, its teaser is an empty string.
    '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []

    # Example approach: Search for all <article> tags (adjust as needed)
    articles = soup.find_all('article')

    for article in articles:
        # Title might be in <h3> or <h2> with specific classes (adjust selector below)
        title_tag = article.find('h3')
        # Teaser might be in a <p> or <span> with a teaser class (adjust as needed)
        teaser_tag = article.find('p')

        title = title_tag.get_text(strip=True) if title_tag else ''
        teaser = teaser_tag.get_text(strip=True) if teaser_tag else ''

        # Only add if there's some text
        if title or teaser:
            stories.append((title, teaser))

    return stories


def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories and save the audio to a file.

    @params:
        stories (list of tuples of strings): A list of (title, teaser) pairs.
        n (int): The index of the story to read.
        filename (str): The filename for the synthesized audio.

    Output: None
    '''
    # Check if n is within range
    if n < 0 or n >= len(stories):
        raise IndexError(f"Story index {n} is out of range. Number of stories: {len(stories)}")

    title, teaser = stories[n]

    # Combine the title and teaser into a single text
    text_to_read = f"Title: {title}\nTeaser: {teaser}"

    # Use gTTS to synthesize the text
    tts = gTTS(text=text_to_read, lang='en')
    tts.save(filename)

    print(f"Saved the synthesized audio for story {n} to '{filename}'.")
