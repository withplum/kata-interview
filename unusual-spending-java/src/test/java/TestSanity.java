import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TestSanity {

    @Test
    public void sanity() {
        Assertions.assertNotEquals("P", "NP");
    }

}
