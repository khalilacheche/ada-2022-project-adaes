# Story
The journey of Wikispeedia began as an observation of the navigation strategies employed by its players. This game, based on Wikipedia, challenges participants to move from a start article to an end article using only Wikipedia hyperlinks. After closely observing players' behavior during the game, we identified a recurring strategy, which piqued our curiosity.

We noticed that players typically start by navigating toward articles that offer the most hyperlink options for their next move. This initial strategy is likely adopted to avoid getting stuck in a dead-end path. As they progress and get closer to their target, players tend to explore more specific topics closely related to their goal. This behavior reveals insights into semantical distances between topics and the logic behind players' choices.

In light of these observations, our story is structured around three core chapters:

Can this behavior be generalized?
What is the semantic meaning of these paths?
Is this strategy optimal?
We believe that analyzing these three dimensions will provide valuable insights into the behavior we've observed.

# What
Our project is focused on analyzing the strategies of Wikispeedia players. The game presents players with a challenge: to reach a target article from a starting article using Wikipedia hyperlinks in the shortest time possible. Our goal was to understand and interpret the navigation behavior of the players to gain insights into their approach.

# How
We conducted our analysis in several key steps:

Step 1: Data loading and preprocessing, including values sanity checks, encoding backtracks, and removing unplayed games. We also created a networkX graph for centrality measure analysis and shortest paths and DataFrames for document embeddings.

Step 2: Investigated different centrality metrics (out-degree, closeness, PageRank), ranked nodes based on the best centrality metric, and plotted the evolution of the chosen metric in players' paths.

Step 3: Defined a distance metric as the shortest path distance from the start point to the end article. Computed this metric for each hop in the path and plotted its evolution.

Step 4: Utilized sBERT to provide vector embeddings of articles, computed cosine similarity between embedded vectors to determine semantic closeness, and investigated whether the shortest path reflects semantic closeness between consecutive hops.

Step 5: Examined whether players get semantically closer to their destination with each hop, plotting the evolution of semantic closeness as they progress in the path.

Step 6: Studied paths that deviated from the typical strategy and analyzed differences in decision-making. We summarized our findings and conclusions in a storytelling format.

# Challenges
Our project involved several challenges, including data preprocessing, centrality metric selection, and addressing the predictability of human behavior. We had to ensure the reproducibility of our analysis and derive meaningful insights from the players' strategies.

# Result
Through our analysis, we aimed to provide a deeper understanding of the behavior of Wikispeedia players and the strategies they employ. By addressing the research questions and conducting a comprehensive analysis, we aimed to shed light on whether this behavior can be generalized, the semantic meaning of players' paths, and the optimality of their strategy.