import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtCharts 

Window {
    width: 800
    height: 800
    visible: true
    title: qsTr("Hello World")

    Rectangle {
        width: 800
        height: 600

        GridView {
            anchors.fill: parent
            cellWidth: 400
            cellHeight: 300
            model: 2

            delegate: Rectangle {
                width: 400
                height: 300

                ChartView {
                    anchors.fill: parent
                    antialiasing: true
                    // animationOptions: ChartView.AllAnimations
                    title: "Chart"

                    LineSeries {
                        name: "Line 1"
                        VXYModelMapper {
                            model: my_model
                            xColumn: 0
                            yColumn: 1
                        }
                    }

                    LineSeries {
                        name: "Line 2"
                        VXYModelMapper {
                            model: my_model
                            xColumn: 2
                            yColumn: 3
                        }
                    }
                }
            }
        }
    }
 
}
