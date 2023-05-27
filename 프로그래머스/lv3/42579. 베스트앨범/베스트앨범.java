import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> totalPlaysByGenre = new HashMap<>();
        HashMap<String, PriorityQueue<int[]>> songsByGenre = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int playCount = plays[i];

            totalPlaysByGenre.put(genre, totalPlaysByGenre.getOrDefault(genre, 0) + playCount);

            if (!songsByGenre.containsKey(genre)) {
                songsByGenre.put(genre, new PriorityQueue<>((a, b) -> {
                    if (a[0] == b[0]) {
                        return a[1] - b[1];
                    }
                    return b[0] - a[0];
                }));
            }

            songsByGenre.get(genre).add(new int[] {playCount, i});
        }

        List<int[]> bestAlbum = new ArrayList<>();

        List<Map.Entry<String, Integer>> sortedGenres = new ArrayList<>(totalPlaysByGenre.entrySet());
        sortedGenres.sort((a, b) -> b.getValue() - a.getValue());

        for (Map.Entry<String, Integer> entry : sortedGenres) {
            String genre = entry.getKey();
            PriorityQueue<int[]> songs = songsByGenre.get(genre);

            if (songs.size() >= 2) {
                bestAlbum.add(songs.poll());
                bestAlbum.add(songs.poll());
            } else {
                bestAlbum.add(songs.poll());
            }
        }

        int[] answer = new int[bestAlbum.size()];
        for (int i = 0; i < bestAlbum.size(); i++) {
            answer[i] = bestAlbum.get(i)[1];
        }

        return answer;
    }
}
