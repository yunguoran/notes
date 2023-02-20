# MISC

## Research

[Google Search Tips](https://www.lifehack.org/articles/technology/20-tips-use-google-search-efficiently.html):

- Use the tabs
- Use quotes
    - "Puppy Dog Sweaters"
    - it will search for that phrase exactly as you typed it
- Use a hyphen to exclude words
    - Mustang -car
    - This tells the search engine to search for mustangs but to remove any results that have the word "car" in it

- Use a colon to search specific sites
    - Sidney Crosby site:nhl.com
    - This will search for all content about famous hockey player Sidney Crosby, but only on NHL.com
- Find a page that links to another page
    - link:nytimes.com
    - That will return all pages that link to the New York Times official website
- Use the asterisk wildcard
    - "Come \*right now\* me"
    - Google search will search for that phrase knowing that the asterisks can be any word
- Find sites that are similar to other sites
    - related:amazon.com
    - you’ll find links to online stores like Amazon
- Search for multiple words at once
    - chocolate OR white chocolate
    - This will search for pages that have either chocolate or white chocolate
- Search a range of numbers
    - What teams have won the Stanley Cup ..2004
        - The two dots with only one number will tell the search that you don’t need anything before or after 2004
    - 41..43
        - Google will search for the numbers 41, 42, and 43.
- Keep it simple
    - Pizza places nearby
    - Google search will grab your location and deliver a variety of results about pizza places that are near you
- Gradually add search terms
    - First try: job interviews
    - Second try: prepare for job interviews
    - Third try: how to prepare for a job interview
- Use words that websites would use
    - "My head hurts" could be replaced by "headache relief"
    - When searching, try to use terminology you would find on a professional website
- Use important words only
    - Don’t use: Where can I find a Chinese restaurant that delivers
    - Instead try: Chinese restaurants nearby
- Google search has shortcuts
    - Weather \*zip code\* – This will show you the weather in the given zip code. You can also use town and city names instead of area codes, but it may not be as accurate if there are multiple area codes in the city.
    - What is \*celebrity name\* Bacon Number – This is a fun little one that will tell you how many connections any given celebrity has to famed actor Kevin Bacon. The popular joke, Six Degrees of Kevin Bacon, is that no actor is more than 6 connections away from Kevin Bacon. Mark Zuckerberg has a Bacon Number of 3.
    - What is the definition of \*word\* or Define: \*word\* – This will display the definition of a word.
    - Time \*place\* – This will display the time in whatever place you type in.
- Use descriptive words
    - If you search for something and you can’t find an answer, try asking the same question using different words and see if that helps the results.
- Find a specific file
    - \*Search term here\* filetype:pdf

## Other

- While exporting data to CSV file, but a field which has values separated by comma, replace comma with linefeed and then double quote the value of this field can solve this issue.
- Use kdocs or markdown table instead of uploading files on gitlab.
- [Zip bomb](https://en.wikipedia.org/wiki/Zip_bomb), [reference from stack overflow: Zip Bomb detected](https://stackoverflow.com/questions/44897500/using-apache-poi-zip-bomb-detected).
- 当升级一个包时，如果依赖的包也需要升级，则也需要查看相应依赖包的 changelog，并做相应测试。
- 只有一个入口方法时，简单的叫做 run 没问题。现在增加了入口方法，第一个方法还叫 run 就不合适了。命名看上下文，尤其注意上下文是会变的，重构、新增代码都需要重新审视上下文。
- 文档只写对客户端有用的，没用的省略。严格来说应该确保不返回，但除非涉及敏感信息，否则一般不做额外处理，文档不暴露即可。对应的，客户端只应该使用文档声明了的字段，未声明的都是随时可改、不需要跟客户端打招呼的。
