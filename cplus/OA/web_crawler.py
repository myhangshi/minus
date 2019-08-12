"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url. 
"""

class Solution:
    """
    @param url(string): a url of root page
    @return (list): all urls
    """
    '''
    def crawler(self, url):
        # write your code here
        to_parse = [url]
        parsed = []
        while to_parse:
            url = to_parse.pop(0)
            if not 'wikipedia' in url:
                continue
            if url in parsed:
                continue
            parsed.append(url)
            to_parse_next = HtmlHelper.parseUrls(url)
            for next_url in to_parse_next:
                if next_url not in to_parse:
                    to_parse.append(next_url)
        return parsed
    '''
    
    def crawler(self, url):
      # write your code here
      if not "wikipedia" in url:
        return False
        
      visited = set()
      visited.add(url)
      
      self.dfs(url, visited)
      return list(visited)
      
    def dfs(self, url, visited):
      url_list = HtmlHelper.parseUrls(url)
      for sub in url_list:
        if self.is_valid(sub, visited):
          visited.add(sub)
          self.dfs(sub, visited)
          
      
    def is_valid(self, url, visited):
      if "wikipedia" in url and url not in visited:
        return True
        
      return False

