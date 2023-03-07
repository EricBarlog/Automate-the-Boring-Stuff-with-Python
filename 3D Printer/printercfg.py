# This file contains common pin mappings for the BIGTREETECH SKR V1.4
# board. To use this config, the firmware should be compiled for the
# LPC1768 or LPC1769(Turbo).

# See docs/Config_Reference.md for a description of parameters.

[include mainsail.cfg]

[stepper_x]
step_pin: P2.2
dir_pin: !P2.6
enable_pin: !P2.1
microsteps: 128
rotation_distance: 40
endstop_pin: !P1.29
position_endstop: 0
position_min: -4
position_max: 250
homing_speed: 100

[stepper_y]
step_pin: P0.19
dir_pin: P0.20
enable_pin: !P2.8
microsteps: 128
rotation_distance: 40
endstop_pin: !P1.28
position_endstop: 0
position_max: 250
homing_speed: 100

[stepper_z]
step_pin: P0.22
dir_pin: P2.11
enable_pin: !P0.21
microsteps: 128
rotation_distance: 8
endstop_pin: probe:z_virtual_endstop
#!P1.27
#position_endstop: 0.0
position_min: -3
position_max: 270
homing_speed: 50

[stepper_z1]
step_pin: P1.15
dir_pin: P1.14
enable_pin: !P1.16
microsteps: 128
rotation_distance: 8

[bltouch]
sensor_pin: ^P0.10 #Probe 
control_pin: P2.0 #Servos
pin_up_touch_mode_reports_triggered: False
x_offset: -2.42
y_offset: -24.78
#z_offset: 5

[safe_z_home]
home_xy_position: 117.5,151.5
speed: 50
z_hop: 4
z_hop_speed: 5

[bed_mesh]
speed: 240 #mm/min
horizontal_move_z: 4
mesh_min: 34,34
mesh_max: 201,201
probe_count: 5,5
mesh_pps: 2,2
algorithm: bicubic
fade_start: 1
fade_end: 10
fade_target: 0

[extruder]
step_pin: P2.13
dir_pin: P0.11
enable_pin: !P2.12
microsteps: 16
rotation_distance: 3.258
nozzle_diameter: 0.400
filament_diameter: 1.750
heater_pin: P2.7
sensor_type: EPCOS 100K B57560G104F
sensor_pin: P0.23
#control: pid
#pid_Kp: 22.2
#pid_Ki: 1.08
#pid_Kd: 114
min_temp: 0
max_temp: 300
pressure_advance: 0.04875


#[extruder1]
#step_pin: P1.15
#dir_pin: P1.14
#enable_pin: !P1.16
#heater_pin: P2.4
#sensor_pin: P0.23
#...

[heater_bed]
heater_pin: P2.5
sensor_type: EPCOS 100K B57560G104F
sensor_pin: P0.25
control: pid
pid_Kp: 54.027
pid_Ki: 0.770
pid_Kd: 948.182
min_temp: 0
max_temp: 130

[fan]
pin: P2.3

[heater_fan Extruder_fan]
pin: P2.4
heater: extruder
heater_temp: 50.0
fan_speed: 1

[mcu]
serial: /dev/serial/by-id/usb-Klipper_lpc1768_0150000948104AAF2692675DC42000F5-if00

[printer]
kinematics: cartesian
max_velocity: 400
max_accel: 3500
max_z_velocity: 12
max_z_accel: 200

########################################
# G_CODE MACROS
########################################

[gcode_macro START_PRINT]
gcode:
    {% set BED_TEMP = params.BED_TEMP|default(60)|float %}
    {% set EXTRUDER_TEMP = params.EXTRUDER_TEMP|default(190)|float %}
    # Start bed heating (but don't wait for it)
    M140 S{BED_TEMP}

    # Use absolute coordinates
    G90
    G28 ; home all axes
    G1 Z5 F5000 ; lift nozzle
    BED_MESH_PROFILE LOAD="default"
    # Wait for bed to reach temperature
    M190 S{BED_TEMP}
    # Set and wait for nozzle to reach temperature
    M109 S{EXTRUDER_TEMP}

    #Purge Line
    G92 E0 ; Reset Extruder
    G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
    G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
    G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line
    G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little
    G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line
    G92 E0 ; Reset Extruder
    #Raise Z Axis and Begin Print
    G1 Z5 F5000 ; lift nozzle

[gcode_arcs]

[gcode_macro END_PRINT]
gcode:
   G91
   # Retract a bit
   G1 E-4 F2700
   G1 E-2 Z0.2 F2400
   G1 X5 Y5 F3000
   # Turn off bed, extruder, and fan
   M140 S0
   M104 S0
   M106 S0
   # Raise nozzle by 10mm
   G1 Z10 F3000
   G90
   # Deliver print
   G1 X0 Y235
   # Disable steppers
   M84 X Y E
   # Clear bed mesh
   BED_MESH_CLEAR
   # Turn off gcode offset
   SET_GCODE_OFFSET Z=0
   M117 Print complete

[pause_resume]

[gcode_macro M600]
gcode:
    {% set X = params.X|default(50)|float %}
    {% set Y = params.Y|default(0)|float %}
    {% set Z = params.Z|default(10)|float %}
    SAVE_GCODE_STATE NAME=M600_state
    PAUSE
    G91
    G1 E-.8 F2700
    G1 Z{Z}
    G90
    G1 X{X} Y{Y} F3000
    G91
    G1 E-50 F1000
    RESTORE_GCODE_STATE NAME=M600_state



########################################
# MISC CONTROL
########################################

# Can control with SET_LED LED=hotend RED=x.x GREEN=x.x BLUE=x.x
[neopixel hotend]
pin: P1.24
chain_count: 2
color_order: GRB
# Set to on-brand BIQU-B1 hot pink
initial_RED: 1.0
initial_GREEN: 0.1
initial_BLUE: 0.8

# Results of manual resonance measuring
[input_shaper]
#shaper_freq_x: 38.76
#shaper_freq_y: 57.69
#shaper_type: mzv

[bed_screws]
screw1: 30,30
screw2: 30,205
screw3: 205,205
screw4: 205,30

[display]
lcd_type: st7920
cs_pin: EXP1_4
sclk_pin: EXP1_5
sid_pin: EXP1_3
encoder_pins: ^EXP2_3, ^EXP2_5
click_pin: ^!EXP1_2
#kill_pin: ^!EXP2_8

[output_pin beeper]
pin: EXP1_1

[z_tilt]
z_positions: -20,103 # Motor Positions
  255,103
points: 15,151.5 # Probe points
#  117.5,151.5
  220,151.5
speed: 250
horizontal_move_z: 5
retries: 20
retry_tolerance: 0.02


########################################
# ADXL345 resonance measurement
########################################

#[mcu rpi]
#serial: /tmp/klipper_host_mcu

#[adxl345]
#cs_pin: rpi:None

#[resonance_tester]
#accel_chip: adxl345
#probe_points:
#    100,100,20  # an example

########################################
# TMC2208 configuration
########################################

[tmc2208 stepper_x]
uart_pin: P1.10
run_current: 0.700
hold_current: 0.500
stealthchop_threshold: 999999

[tmc2208 stepper_y]
uart_pin: P1.9
run_current: 0.700
hold_current: 0.500
stealthchop_threshold: 999999

[tmc2208 stepper_z1] #original
uart_pin: P1.8
run_current: 0.800
hold_current: 0.500
stealthchop_threshold: 999999

[tmc2208 extruder]
uart_pin: P1.4
run_current: 0.700
hold_current: 0.500
stealthchop_threshold: 999999

[tmc2208 stepper_z]
uart_pin: P1.1
run_current: 0.800
hold_current: 0.500
stealthchop_threshold: 999999


########################################
# TMC2130 configuration
########################################

#[tmc2130 stepper_x]
#cs_pin: P1.10
#spi_software_miso_pin: P0.5
#spi_software_mosi_pin: P1.17
#spi_software_sclk_pin: P0.4
#run_current: 0.800
#stealthchop_threshold: 999999
#diag1_pin: P1.29

#[tmc2130 stepper_y]
#cs_pin: P1.9
#spi_software_miso_pin: P0.5
#spi_software_mosi_pin: P1.17
#spi_software_sclk_pin: P0.4
#run_current: 0.800
#stealthchop_threshold: 999999
#diag1_pin: P1.28

#[tmc2130 stepper_z]
#cs_pin: P1.8
#spi_software_miso_pin: P0.5
#spi_software_mosi_pin: P1.17
#spi_software_sclk_pin: P0.4
#run_current: 0.650
#stealthchop_threshold: 999999
#diag1_pin: P1.27

#[tmc2130 extruder]
#cs_pin: P1.4
#spi_software_miso_pin: P0.5
#spi_software_mosi_pin: P1.17
#spi_software_sclk_pin: P0.4
#run_current: 0.800
#stealthchop_threshold: 999999
#diag1_pin: P1.26

#[tmc2130 extruder1]
#cs_pin: P1.1
#spi_software_miso_pin: P0.5
#spi_software_mosi_pin: P1.17
#spi_software_sclk_pin: P0.4
#run_current: 0.800
#stealthchop_threshold: 999999
#diag1_pin: P1.25


########################################
# EXP1 / EXP2 (display) pins
########################################

[board_pins]
aliases:
    # EXP1 header
    EXP1_1=P1.30, EXP1_3=P1.18, EXP1_5=P1.20, EXP1_7=P1.22, EXP1_9=<GND>,
    EXP1_2=P0.28, EXP1_4=P1.19, EXP1_6=P1.21, EXP1_8=P1.23, EXP1_10=<5V>,
    # EXP2 header
    EXP2_1=P0.17, EXP2_3=P3.26, EXP2_5=P3.25, EXP2_7=P1.31, EXP2_9=<GND>,
    EXP2_2=P0.15, EXP2_4=P0.16, EXP2_6=P0.18, EXP2_8=<RST>, EXP2_10=<NC>
    # Pins EXP2_1, EXP2_6, EXP2_2 are also MISO, MOSI, SCK of bus "ssp0"

# See the sample-lcd.cfg file for definitions of common LCD displays.

#*# <---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
#*# [bltouch]
#*# z_offset = 2.290
#*#
#*# [bed_mesh default]
#*# version = 1
#*# points =
#*# 	  -0.092188, -0.080938, -0.039688, 0.098750, 0.131875
#*# 	  -0.101875, -0.083750, -0.025625, 0.129687, 0.148750
#*# 	  -0.079688, -0.072813, -0.013750, 0.116250, 0.139062
#*# 	  -0.047813, -0.028125, 0.012500, 0.134062, 0.133437
#*# 	  -0.039375, -0.010625, 0.036562, 0.163437, 0.185937
#*# x_count = 5
#*# y_count = 5
#*# mesh_x_pps = 2
#*# mesh_y_pps = 2
#*# algo = bicubic
#*# tension = 0.2
#*# min_x = 34.0
#*# max_x = 201.0
#*# min_y = 34.0
#*# max_y = 201.0
#*#
#*# [extruder]
#*# control = pid
#*# pid_kp = 28.875
#*# pid_ki = 1.385
#*# pid_kd = 150.512
