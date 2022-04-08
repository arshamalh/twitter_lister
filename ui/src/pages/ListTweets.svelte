<script>
  import { onMount } from "svelte";
  import { BaseURL } from "../stores";
  import TweetCard from "../components/TweetCard.svelte";

  let tweets = [];

  onMount(async () => {
    const response = await fetch($BaseURL + "/get_liked_tweets", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ search_query: "" }),
    }).then((res) => res.json());
    if (response.code === 200 && response.data.length > 0) {
      tweets = response.data;
      console.log(tweets);
    }
  });
</script>

<section>
  {#each tweets as tweet}
    <TweetCard {tweet} />
  {/each}
</section>

<style>
  section {
    display: flex;
    flex-wrap: wrap;
    gap: 1%;
  }
</style>
