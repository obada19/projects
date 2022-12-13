import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;
public class textfield implements ActionListener {
    JTextField textField_for_price, textField_for_costumer, textField_for_volume, textField_for_special_discount;
    JButton button_for_calculate, button_for_costumer, button_for_volume, button_for_special_discount;


    textfield() {
        JFrame frame = new JFrame("product price calculator");
        textField_for_price = new JTextField();
        textField_for_price.setBounds(50, 50, 150, 20);
        textField_for_costumer = new JTextField();
        textField_for_costumer.setBounds(50, 100, 150, 20);
        textField_for_volume = new JTextField();
        textField_for_volume.setBounds(50, 150, 150, 20);
        textField_for_special_discount = new JTextField();
        textField_for_special_discount.setBounds(50, 200, 150, 20);
        button_for_calculate = new JButton("offer price");
        button_for_costumer = new JButton("costumer");
        button_for_volume = new JButton("volume calculate");
        button_for_special_discount = new JButton(" special discount calculate");
        button_for_calculate.setBounds(200, 50, 150, 20);
        button_for_costumer.setBounds(200, 100, 150, 20);
        button_for_volume.setBounds(200, 150, 150, 20);
        button_for_special_discount.setBounds(200, 200, 150, 20);
        button_for_calculate.addActionListener(this);
        button_for_costumer.addActionListener(this);
        button_for_volume.addActionListener(this);
        button_for_special_discount.addActionListener(this);
        frame.add(textField_for_price);
        frame.add(textField_for_costumer);
        frame.add(textField_for_volume);
        frame.add(textField_for_special_discount);
        frame.add(button_for_calculate);
        frame.add(button_for_costumer);
        frame.add(button_for_volume);
        frame.add(button_for_special_discount);
        frame.setSize(500, 500);
        frame.setLayout(null);
        frame.setVisible(true);
    }



    public void actionPerformed(ActionEvent e) {

        String text_product = textField_for_price.getText();
        String text_costumer = textField_for_costumer.getText();
        String text_volume = textField_for_volume.getText();
        String text_special_discount = textField_for_special_discount.getText();


        if (e.getSource() == button_for_calculate)
        {
            product_price.calculator(text_product);

        }
        else if (e.getSource()==button_for_costumer)
        {
            calculate_price_costumer.costumer(text_costumer, text_product);
        }
        else if(e.getSource()==button_for_volume) {


            int text_volume_integer = Integer.parseInt(text_volume);
            volume_discount.offer(text_volume_integer);


        }
        else if (e.getSource()==button_for_special_discount)
        {
            int rebated_price = (int) volume_discount.rebated_price;
            special_discount.offer(rebated_price, text_special_discount);
        }
        else
        {
            JOptionPane.showMessageDialog(null, "no product was found"+ text_product);
        }
        }
    }
