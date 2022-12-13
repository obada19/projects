import javax.swing.*;

public class volume_discount extends calculate_price_costumer {
    static int the_price_with_volume_rebate;
    public static void offer(int text_volume_integer) {
            if (text_volume_integer >= 100) {
                //  adding a 10% discount
                the_price_with_volume_rebate = (int) (rebated_price * 0.90);
                JOptionPane.showMessageDialog(null, "The price if purchasing with such volume is : " + the_price_with_volume_rebate);
            } else {
                JOptionPane.showMessageDialog(null, "This volume has no discount");
            }

    }
}
