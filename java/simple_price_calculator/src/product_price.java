import javax.swing.*;

public class product_price {
    public static int calculator(String text_product) {
        Integer product_name_checker = new Products().products_and_prices.get(text_product);
        int price = 0;
        if (product_name_checker != null) {
            price = new Products().products_and_prices.get(text_product);
            JOptionPane.showMessageDialog(null, "The price " + price);

        } else {
            JOptionPane.showMessageDialog(null, "This product was found");
        }
        return price;
    }
}
