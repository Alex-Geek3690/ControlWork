package work_2;

public class Toy {
    private final String id;
    private final String name;
    private final int drop_frequency;

    public Toy(String id, String name, int drop_frequency) {
        this.id = id;
        this.name = name;
        this.drop_frequency = drop_frequency;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getDrop_frequency() {
        return drop_frequency;
    }

}