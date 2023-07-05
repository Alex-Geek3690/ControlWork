package work_2;

import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        Toy toy_1 = new Toy("1", "игрушка1", 20);
        Toy toy_2 = new Toy("2", "игрушка2", 30);
        Toy toy_3 = new Toy("3", "игрушка3", 50);

        PriorityQueue<Toy> queue = new PriorityQueue<>((t1, t2) -> t2.getDrop_frequency() - t1.getDrop_frequency());
        queue.add(toy_1);
        queue.add(toy_2);
        queue.add(toy_3);

        StringBuilder res = new StringBuilder();
        for (int i = 0; i < 30; i++) {
            Toy random_toy = getRandom(queue);
            res.append(random_toy.getId()).append(" ").append(random_toy.getName()).append("\n");
        }

        writeToFile("file.txt", res.toString());

    }

    private static Toy getRandom(PriorityQueue<Toy> queue){
        int number = (int) (Math.random()*100);
        int cumDroprate = 0;
        for (Toy toy : queue) {
            cumDroprate += toy.getDrop_frequency();
            if (number < cumDroprate) {
                return toy;
            }
        }
        return null;
    }

    private static void writeToFile(String filename, String content){
        try (FileWriter writer = new FileWriter(filename)){
            writer.write(content);
        } catch (IOException e){
            e.printStackTrace();
        }
    }

}
