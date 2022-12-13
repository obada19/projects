import javax.swing.*;
import java.util.Objects;

public class special_discount extends calculate_price_costumer{
 public static void offer(int rebated_price, String text_special_discount) {
         if (Objects.equals(text_special_discount, "høstferie")) {
             int the_price_with_special_discount = (int) (rebated_price * 0.80);
             JOptionPane.showMessageDialog(null, "The price if purchasing with høstferie code: " + the_price_with_special_discount);


         } else {
             JOptionPane.showMessageDialog(null, "There are no special discounts");

         }

     }
 }
