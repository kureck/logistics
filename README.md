

curl -i -H "Content-Type: application/json" -X POST -d '{"road_map":1, "origin": "A", "destination":"D", "autonomia": 10, "litro":2.5 }' http://127.0.0.1:8000/shortest_path/api/map/find_shortest_path/