Basic Graph:
In this basic graph, we represent the entities (Michelin, T40, Peugeot, Toyota, Peugeot 306, and Toyota Supra) as nodes in the graph, and the relationships between them as edges. The labels on the edges represent the type of relationship between the entities.


   (Michelin) ---[is a]---> (Manufacturer) ---[makes]---> (Tires) ---[has model]---> (T40)
                    |                                   |                           |
                    |                                   |                           |
                    +-----[can be fixed on]---------------+                           |
                                                                                        |
                                                                                        |
                                                                                    (Products)
                    |                                   |                           |
                    |                                   |                           |
                    +-----[uses]--------------------------+                           |
                                |                                                       |
                                |                                                       |
                          (Peugeot 306)                               (Toyota Supra)

                          
Improved Graph:
In this improved graph, we represent the entities as nodes, and the relationships between them as edges with additional labels that capture more information about the relationships. We also use different types of edges to represent different types of relationships.
                                      (Michelin)
                                          |
                                          |
                            +-------------[is a manufacturer of]-------------+
                            |                                               |
                       (Tires)                                            (Countries)
                            |                                               |
                            |                                               |
          +----------------[has model T40 that can be fixed on]--------------+
          |                                                                 |
          |                                                                 |
     (Peugeot)                                                        (Toyota)
          |                                                                 |
          |                                                                 |
          +---------[T40 model's durability is average for]-----------------+
                              |                                             |
                              |                                             |
                         (Peugeot 306)                               (Toyota Supra)
In this graph, we distinguish between different types of relationships: Michelin is a manufacturer of tires; the T40 model of tires can be fixed on Peugeot and Toyota products; the durability of the T40 model is average for Peugeot 306 cars and optimal for Toyota Supra cars. We also add additional nodes for countries, which allow us to capture information about where Michelin operates.