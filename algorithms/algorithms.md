# Algorithms

## Sorting

[Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/?ref=lbp).

## Split SQL Text

```java
  /*
   * Reference from Zeppelin, used to split multiple SQL statements.
   */
  private List<String> splitSql(String text) {
    text = text.trim();
    List<String> queries = new ArrayList<>();
    StringBuilder query = new StringBuilder();
    char character;

    boolean multiLineComment = false;
    boolean singleLineComment = false;
    boolean singleQuoteString = false;
    boolean doubleQuoteString = false;

    for (int index = 0; index < text.length(); index++) {
      character = text.charAt(index);

      // end of single line comment
      if (singleLineComment && (character == '\n')) {
        singleLineComment = false;
        if (query.toString().trim().isEmpty()) {
          continue;
        }
      }

      // end of multiple line comment
      if (multiLineComment && character == '/' && text.charAt(index - 1) == '*') {
        multiLineComment = false;
        if (query.toString().trim().isEmpty()) {
          continue;
        }
      }

      if (character == '\'') {
        if (singleQuoteString) {
          singleQuoteString = false;
        } else if (!doubleQuoteString) {
          singleQuoteString = true;
        }
      }

      if (character == '"') {
        if (doubleQuoteString && index > 0) {
          doubleQuoteString = false;
        } else if (!singleQuoteString) {
          doubleQuoteString = true;
        }
      }

      if (!singleQuoteString && !doubleQuoteString && !multiLineComment && !singleLineComment
        && text.length() > (index + 1)) {
        if (isSingleLineComment(text.charAt(index), text.charAt(index + 1))) {
          singleLineComment = true;
        } else if (text.charAt(index) == '/' && text.charAt(index + 1) == '*') {
          multiLineComment = true;
        }
      }

      if (character == ';' && !singleQuoteString && !doubleQuoteString && !multiLineComment
        && !singleLineComment) {
        // meet semicolon
        queries.add(query.toString().trim());
        query = new StringBuilder();
      } else if (index == (text.length() - 1)) {
        // meet the last character
        if (!singleLineComment && !multiLineComment) {
          query.append(character);
          queries.add(query.toString().trim());
        }
      } else if (!singleLineComment && !multiLineComment) {
        // normal case, not in single line comment and not in multiple line comment
        query.append(character);
      } else if (singleLineComment && !query.toString().trim().isEmpty()) {
        // in single line comment, only add it to query when the single line comment is
        // in the middle of sql statement
        // e.g.
        // select a -- comment
        // from table_1
        query.append(character);
      } else if (multiLineComment && !query.toString().trim().isEmpty()) {
        // in multiple line comment, only add it to query when the multiple line comment
        // is in the middle of sql statement.
        // e.g.
        // select a /* comment */
        // from table_1
        query.append(character);
      }
    }

    return queries;
  }

  private boolean isSingleLineComment(char curChar, char nextChar) {
    // In Zeppelin, you can customize the prefix.
    // @see <a href="https://github.com/apache/zeppelin/blob/e0e2ca5f8087d8f47a9fba4bfe736b53a565cb11/zeppelin-interpreter/src/main/java/org/apache/zeppelin/interpreter/util/SqlSplitter.java#L199">Zeppelin</a>
    String singleCommentPrefix = "--";
    if (curChar == singleCommentPrefix.charAt(0) &&
      nextChar == singleCommentPrefix.charAt(1)) {
      return true;
    }
    return false;
  }
```
