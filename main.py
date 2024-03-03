from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from math import *


def main():
    app = QApplication([])

    main_window = QWidget()
    main_window.setWindowIcon(QIcon('assets/icon.ico'))
    main_window.setFixedSize(500, 400)
    main_window.setWindowTitle('Geometry calculator')

    # -------------- Figure list ----------------

    figure_list = []

    def show_figure(figure_name):
        for figure in figure_list:
            for widget in figure:
                widget.hide()

        for widget in figure_name:
            widget.show()

    square = []
    square_perimeter = None
    square_area = None
    figure_list.append(square)

    rectangle = []
    rectangle_perimeter = None
    rectangle_area = None
    figure_list.append(rectangle)

    triangle = []
    triangle_perimeter = None
    triangle_area = None
    figure_list.append(triangle)

    circle = []
    circle_perimeter = None
    circle_area = None
    figure_list.append(circle)

    # -------------------------------------------

    def change_figure(text):
        if text == 'Square':
            show_figure(square)
            area_value.setText(square_area)
            perimeter_value.setText(square_perimeter)
        if text == 'Triangle':
            show_figure(triangle)
            area_value.setText(triangle_area)
            perimeter_value.setText(triangle_perimeter)
        if text == 'Rectangle':
            show_figure(rectangle)
            area_value.setText(rectangle_area)
            perimeter_value.setText(rectangle_perimeter)
        if text == 'Circle':
            show_figure(circle)
            area_value.setText(circle_area)
            perimeter_value.setText(circle_perimeter)

    def calculate_area():
        nonlocal square_area, triangle_area, rectangle_area, circle_area

        a = enter_a_field.text()
        b = enter_b_field.text()
        c = enter_c_field.text()
        h = enter_h_field.text()
        r = enter_radius_field.text()

        if choose_figure_box.currentText() == 'Square':
            if a != '' and int(a) > 0:
                square_area = str(int(a) ** 2)
                area_value.setText(square_area)
        if choose_figure_box.currentText() == 'Triangle':
            if a != '' and int(a) > 0:
                if h != '' and int(h) > 0:
                    triangle_area = str((int(a) * int(h)) / 2)
                    area_value.setText(triangle_area)
                elif b != '' and int(b) > 0 and c != '' and 0 < int(c) < int(a) + int(
                        b) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
                    p = (int(a) + int(b) + int(c)) / 2
                    non_sqrt_area = p * (p - int(a)) * (p - int(b)) * (p - int(c))
                    triangle_area = str(sqrt(non_sqrt_area))
                    area_value.setText(triangle_area)
        if choose_figure_box.currentText() == 'Rectangle':
            if a != '' and int(a) > 0 and b != '' and int(b) > 0:
                rectangle_area = str(int(a) * int(b))
                area_value.setText(rectangle_area)
        if choose_figure_box.currentText() == 'Circle':
            if r != '' and int(r) > 0:
                circle_area = str(round(pi, 2) * (int(r) ** 2))
                area_value.setText(circle_area)

    def calculate_perimeter():
        nonlocal square_perimeter, triangle_perimeter, rectangle_perimeter, circle_perimeter

        a = enter_a_field.text()
        b = enter_b_field.text()
        c = enter_c_field.text()
        r = enter_radius_field.text()

        if choose_figure_box.currentText() == 'Square':
            if a != '' and int(a) > 0:
                square_perimeter = str(int(a) * 4)
                perimeter_value.setText(square_perimeter)
        if choose_figure_box.currentText() == 'Triangle':
            if b != '' and int(b) > 0 and c != '' and 0 < int(c) < int(a) + int(
                    b) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
                triangle_perimeter = str(int(a) + int(b) + int(c))
                perimeter_value.setText(triangle_perimeter)
        if choose_figure_box.currentText() == 'Rectangle':
            if a != '' and int(a) > 0 and b != '' and int(b) > 0:
                rectangle_perimeter = str(int(a) * 2 + int(b) * 2)
                perimeter_value.setText(rectangle_perimeter)
        if choose_figure_box.currentText() == 'Circle':
            if r != '' and int(r) > 0:
                circle_perimeter = str(round(pi, 2) * 2 * int(r))
                perimeter_value.setText(circle_perimeter)

    # ----------- Main window section -----------

    calculate_area_button = QPushButton(main_window)
    calculate_area_button.setText('Calculate Area')
    calculate_area_button.resize(100, 21)
    calculate_area_button.move(380, 360)
    calculate_area_button.clicked.connect(calculate_area)

    calculate_perimeter_button = QPushButton(main_window)
    calculate_perimeter_button.setText('Calculate Perimeter')
    calculate_perimeter_button.resize(120, 21)
    calculate_perimeter_button.move(360, 335)
    calculate_perimeter_button.clicked.connect(calculate_perimeter)

    perimeter_equals = QLabel(main_window)
    perimeter_equals.setText('Perimeter = ')
    perimeter_equals.move(20, 340)

    perimeter_value = QLabel(main_window)
    perimeter_value.resize(100, 13)
    perimeter_value.move(80, 340)

    area_equals = QLabel(main_window)
    area_equals.setText('Area = ')
    area_equals.move(20, 360)

    area_value = QLabel(main_window)
    area_value.resize(100, 13)
    area_value.move(58, 360)

    choose_figure = QLabel(main_window)
    choose_figure.setText('Choose a figure:')
    choose_figure.move(20, 20)

    choose_figure_box = QComboBox(main_window)
    choose_figure_box.addItem('Square')
    choose_figure_box.addItem('Triangle')
    choose_figure_box.addItem('Rectangle')
    choose_figure_box.addItem('Circle')
    choose_figure_box.resize(100, 20)
    choose_figure_box.move(20, 40)
    choose_figure_box.currentTextChanged.connect(change_figure)

    formulas = QLabel(main_window)
    formulas.setText('Formulas(P - perimeter, S - area):')
    formulas.move(150, 20)

    square_perimeter_formula = QLabel(main_window)
    square_perimeter_formula.setText('P = a * 4')
    square_perimeter_formula.move(150, 40)
    square.append(square_perimeter_formula)

    square_area_formula = QLabel(main_window)
    square_area_formula.setText('S = a²')
    square_area_formula.move(150, 60)
    square.append(square_area_formula)

    triangle_perimeter_formula = QLabel(main_window)
    triangle_perimeter_formula.setText('P = a + b + c')
    triangle_perimeter_formula.move(150, 40)
    triangle.append(triangle_perimeter_formula)

    first_triangle_area_formula = QLabel(main_window)
    first_triangle_area_formula.setText('S₁ = (a * h)/2')
    first_triangle_area_formula.move(150, 60)
    triangle.append(first_triangle_area_formula)

    second_triangle_formula = QLabel(main_window)
    second_triangle_formula.setText('S₂ = √p (p-a) (p-b) (p-c)   (p = P/2)')
    second_triangle_formula.move(150, 80)
    triangle.append(second_triangle_formula)

    rectangle_perimeter_formula = QLabel(main_window)
    rectangle_perimeter_formula.setText('P = a * 2 + b * 2')
    rectangle_perimeter_formula.move(150, 40)
    rectangle.append(rectangle_perimeter_formula)

    rectangle_area_formula = QLabel(main_window)
    rectangle_area_formula.setText('S = a * b')
    rectangle_area_formula.move(150, 60)
    rectangle.append(rectangle_area_formula)

    circle_perimeter_formula = QLabel(main_window)
    circle_perimeter_formula.setText('P = π * r * 2')
    circle_perimeter_formula.move(150, 40)
    circle.append(circle_perimeter_formula)

    circle_area_formula = QLabel(main_window)
    circle_area_formula.setText('S = π * r²')
    circle_area_formula.move(150, 60)
    circle.append(circle_area_formula)

    enter_values = QLabel(main_window)
    enter_values.setText('Enter values:')
    enter_values.move(350, 20)

    enter_a = QLabel(main_window)
    enter_a.setText('a =')
    enter_a.move(350, 43)
    square.append(enter_a)
    triangle.append(enter_a)
    rectangle.append(enter_a)

    enter_a_field = QLineEdit(main_window)
    enter_a_field.resize(100, 19)
    enter_a_field.move(370, 40)
    square.append(enter_a_field)
    triangle.append(enter_a_field)
    rectangle.append(enter_a_field)

    enter_b = QLabel(main_window)
    enter_b.setText('b =')
    enter_b.move(350, 73)
    triangle.append(enter_b)
    rectangle.append(enter_b)

    enter_b_field = QLineEdit(main_window)
    enter_b_field.resize(100, 19)
    enter_b_field.move(370, 70)
    triangle.append(enter_b_field)
    rectangle.append(enter_b_field)

    enter_c = QLabel(main_window)
    enter_c.setText('c =')
    enter_c.move(350, 103)
    triangle.append(enter_c)

    enter_c_field = QLineEdit(main_window)
    enter_c_field.resize(100, 19)
    enter_c_field.move(370, 100)
    triangle.append(enter_c_field)

    enter_h = QLabel(main_window)
    enter_h.setText('h =')
    enter_h.move(350, 133)
    triangle.append(enter_h)

    if_h_is_given = QLabel(main_window)
    if_h_is_given.setText('(if h is given area is calcu-\nlated with (a*h)/2 formula)')
    if_h_is_given.move(350, 155)
    triangle.append(if_h_is_given)

    enter_h_field = QLineEdit(main_window)
    enter_h_field.resize(100, 19)
    enter_h_field.move(370, 130)
    triangle.append(enter_h_field)

    enter_radius = QLabel(main_window)
    enter_radius.setText('r =')
    enter_radius.move(350, 43)
    circle.append(enter_radius)

    enter_radius_field = QLineEdit(main_window)
    enter_radius_field.resize(100, 19)
    enter_radius_field.move(370, 40)
    circle.append(enter_radius_field)

    square_image = QLabel(main_window)
    square_pixmap = QPixmap('assets/Square_py.png')
    square_pixmap = square_pixmap.scaled(400, 220, Qt.KeepAspectRatio)
    square_image.setPixmap(square_pixmap)
    square_image.move(10, 110)
    square.append(square_image)

    triangle_image = QLabel(main_window)
    triangle_pixmap = QPixmap('assets/Triangle_py.png')
    triangle_pixmap = triangle_pixmap.scaled(400, 220, Qt.KeepAspectRatio)
    triangle_image.setPixmap(triangle_pixmap)
    triangle_image.move(10, 110)
    triangle.append(triangle_image)

    rectangle_image = QLabel(main_window)
    rectangle_pixmap = QPixmap('assets/Rectangle_py.png')
    rectangle_pixmap = rectangle_pixmap.scaled(400, 220, Qt.KeepAspectRatio)
    rectangle_image.setPixmap(rectangle_pixmap)
    rectangle_image.move(10, 110)
    rectangle.append(rectangle_image)

    circle_image = QLabel(main_window)
    circle_pixmap = QPixmap('assets/Circle_py.png')
    circle_pixmap = circle_pixmap.scaled(400, 220, Qt.KeepAspectRatio)
    circle_image.setPixmap(circle_pixmap)
    circle_image.move(10, 110)
    circle.append(circle_image)

    # -------------------------------------------

    main_window.show()
    show_figure(square)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
