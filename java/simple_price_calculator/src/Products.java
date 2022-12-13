import java.util.*;
public class Products {
    Map<String, Integer> products_and_prices;

    public Products() {
        products_and_prices = new HashMap<String, Integer>();
        products_and_prices.put("product_A", 100);
        products_and_prices.put("product_B", 200);
        products_and_prices.put("product_C", 300);
        products_and_prices.put("product_D", 400);
    }
}
