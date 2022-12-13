import javax.swing.*;

public class calculate_price_costumer{
    static float rebated_price;
    public static void costumer(String text_costumer, String text_product) {
        Integer costumer_name_checker = new costumers().costumer_and_rebate.get(text_costumer);
        if (costumer_name_checker != null) {
            Integer rebate = new costumers().costumer_and_rebate.get(text_costumer);
            rebated_price = ((1 - ((float) rebate / 100)) * product_price.calculator(text_product));
            JOptionPane.showMessageDialog(null, "The price for " + text_costumer + new java.text.DecimalFormat("#").format(rebated_price));
        } else {
            JOptionPane.showMessageDialog(null, "This costumer has no rebate agreement and the price is therefore full");
        }
    }
}
