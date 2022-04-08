<script>
  export let tweet;
  function replace_hashtags(text) {
    return text.replace(/(#([\w]+))/g, '<a href="/tags/$2">$1</a>');
  }

  function replace_links(text) {
    return text.replace(
      /(https?:\/\/[^\s]+)/g,
      '<a href="$1" target="_blank">$1</a>'
    );
  }

  function replace_mentions(text) {
    return text.replace(
      /(^|\s)(@([a-zA-Z0-9_]+))/g,
      '$1<a href="/users/$3">$2</a>'
    );
  }

  function renderHTML(text) {
    text = replace_hashtags(text);
    text = replace_links(text);
    text = replace_mentions(text);
    return text;
  }
</script>

<div>
  <p>
    {@html renderHTML(tweet.tweet_text)}
  </p>
</div>

<style>
  div {
    background-color: rgb(202, 247, 255);
    max-width: 19%;
    min-width: 200px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #000;
    border-radius: 10px;
    word-wrap: break-word;
  }
</style>
