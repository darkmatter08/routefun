# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class ObdCardata(models.Model):
    idlogdata = models.IntegerField(db_column='idLogData', primary_key=True) # Field name made lowercase.
    idfiles = models.IntegerField(db_column='idFiles', blank=True, null=True) # Field name made lowercase.
    idtrips = models.ForeignKey('ObdTripsEnh', db_column='idTrips', blank=True, null=True) # Field name made lowercase.
    idvehicles = models.ForeignKey('ObdTripsEnh', db_column='idVehicles', blank=True, null=True) # Field name made lowercase.
    gps_time = models.CharField(db_column='GPS_Time', max_length=50, blank=True) # Field name made lowercase.
    device_time = models.DateTimeField(db_column='Device_Time', blank=True, null=True) # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True) # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True) # Field name made lowercase.
    gps_speed_meters_second = models.FloatField(db_column='GPS_Speed__Meters_second', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    absolute_throttle_position_b = models.FloatField(db_column='Absolute_Throttle_Position_B', blank=True, null=True) # Field name made lowercase.
    accelerator_pedalposition_d = models.FloatField(db_column='Accelerator_PedalPosition_D', blank=True, null=True) # Field name made lowercase.
    ambient_air_temp_f = models.FloatField(db_column='Ambient_air_temp_F', blank=True, null=True) # Field name made lowercase.
    barometric_pressure_from_vehicle_psi = models.FloatField(db_column='Barometric_pressure__from_vehicle__psi', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    engine_load = models.FloatField(db_column='Engine_Load', blank=True, null=True) # Field name made lowercase.
    engine_load_absolute = models.FloatField(db_column='Engine_Load_Absolute', blank=True, null=True) # Field name made lowercase.
    gps_accuracy_ft = models.FloatField(db_column='GPS_Accuracy_ft', blank=True, null=True) # Field name made lowercase.
    gps_altitude_ft = models.FloatField(db_column='GPS_Altitude_ft', blank=True, null=True) # Field name made lowercase.
    gps_bearing = models.FloatField(db_column='GPS_Bearing', blank=True, null=True) # Field name made lowercase.
    gps_satellites = models.IntegerField(db_column='GPS_Satellites', blank=True, null=True) # Field name made lowercase.
    run_time_since_engine_start_s = models.IntegerField(db_column='Run_time_since_engine_start_s', blank=True, null=True) # Field name made lowercase.
    speed_obd_mph = models.FloatField(db_column='Speed__OBD__mph', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    acceleration_sensor_total_g = models.FloatField(db_column='Acceleration_Sensor_Total__g', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    acceleration_sensor_x_axis_g = models.FloatField(db_column='Acceleration_Sensor_X_axis__g', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    acceleration_sensor_y_axis_g = models.FloatField(db_column='Acceleration_Sensor_Y_axis__g', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    acceleration_sensor_z_axis_g = models.FloatField(db_column='Acceleration_Sensor_Z_axis__g', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fuel_flow_rate_hour_gal_hr = models.FloatField(db_column='Fuel_flow_rate_hour_gal_hr', blank=True, null=True) # Field name made lowercase.
    fuel_used_trip_gal = models.FloatField(db_column='Fuel_used__trip__gal', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    fuel_level_from_engine_ecu = models.FloatField(db_column='Fuel_Level__From_Engine_ECU', blank=True, null=True) # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    mass_air_flow_rate_g_s = models.FloatField(db_column='Mass_Air_Flow_Rate_g_s', blank=True, null=True) # Field name made lowercase.
    engine_fuel_rate_l_h = models.FloatField(db_column='Engine_fuel_rate_L_h', blank=True, null=True) # Field name made lowercase.
    distance_travelled_since_codes_cleared_miles = models.FloatField(db_column='Distance_travelled_since_codes_cleared_miles', blank=True, null=True) # Field name made lowercase.
    distance_travelled_with_mil_cel_lit_miles = models.FloatField(db_column='Distance_travelled_with_MIL_CEL_lit_miles', blank=True, null=True) # Field name made lowercase.
    engine_rpm_rpm = models.FloatField(db_column='Engine_RPM_rpm', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'OBD_CarData'

class ObdTripsEnh(models.Model):
    idtrips = models.IntegerField(db_column='idTrips') # Field name made lowercase.
    idvehicles = models.IntegerField(db_column='idVehicles') # Field name made lowercase.
    ranking = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'OBD_Trips_enh'

class RpmTable(models.Model):
    idtrips = models.IntegerField(db_column='idTrips') # Field name made lowercase.
    idvehicles = models.IntegerField(db_column='idVehicles') # Field name made lowercase.
    rpmranking = models.FloatField(db_column='RPMRanking', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RPM_Table'

class Gforceranking(models.Model):
    idtrips = models.IntegerField(db_column='idTrips') # Field name made lowercase.
    idvehicles = models.IntegerField(db_column='idVehicles') # Field name made lowercase.
    granking = models.FloatField(db_column='gRanking', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'gForceRanking'

