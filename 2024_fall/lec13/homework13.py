import bs4
import gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.

    @params:
    text (string): the text of a webpage

    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    try:
        soup = bs4.BeautifulSoup(text, 'html.parser')
        stories = []

        # Find all story elements (adjust the class names based on actual webpage structure)
        for story in soup.find_all('div', class_='story'):  # Update 'div' and 'class_' based on actual HTML
            title_tag = story.find('h1', class_='title') or story.find('h2', class_='title')
            teaser_tag = story.find('p', class_='teaser')

            title = title_tag.get_text(strip=True) if title_tag else ""
            teaser = teaser_tag.get_text(strip=True) if teaser_tag else ""

            stories.append((title, teaser))

        return stories

    except Exception as e:
        raise RuntimeError(f"Error extracting stories: {e}")

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.

    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    try:
        if n < 0 or n >= len(stories):
            raise IndexError("Story index is out of range.")

        title, teaser = stories[n]
        content = f"Title: {title}. Teaser: {teaser}" if teaser else f"Title: {title}."

        # Synthesize speech and save to file
        tts = gtts.gTTS(text=content, lang='en')
        tts.save(filename)

        print(f"Synthesized story saved to {filename}")

    except IndexError as ie:
        raise ValueError(f"Invalid story index: {ie}")
    except Exception as e:
        raise RuntimeError(f"Error reading story: {e}")