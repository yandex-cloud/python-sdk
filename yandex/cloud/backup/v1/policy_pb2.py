# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/backup/v1/policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/backup/v1/policy.proto\x12\x16yandex.cloud.backup.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xfc\x01\n\x06Policy\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x04name\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x65nabled\x18\x05 \x01(\x08\x12\x38\n\x08settings\x18\x06 \x01(\x0b\x32&.yandex.cloud.backup.v1.PolicySettings\x12\x11\n\tfolder_id\x18\x07 \x01(\t\"\xef\x1e\n\x0ePolicySettings\x12M\n\x0b\x63ompression\x18\x01 \x01(\x0e\x32\x32.yandex.cloud.backup.v1.PolicySettings.CompressionB\x04\xe8\xc7\x31\x01\x12\x34\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x1e.yandex.cloud.backup.v1.FormatB\x04\xe8\xc7\x31\x01\x12)\n!multi_volume_snapshotting_enabled\x18\x03 \x01(\x08\x12\'\n\x1fpreserve_file_security_settings\x18\x04 \x01(\x08\x12U\n\nreattempts\x18\x05 \x01(\x0b\x32;.yandex.cloud.backup.v1.PolicySettings.RetriesConfigurationB\x04\xe8\xc7\x31\x01\x12\x1b\n\x13silent_mode_enabled\x18\x06 \x01(\x08\x12I\n\tsplitting\x18\x07 \x01(\x0b\x32\x30.yandex.cloud.backup.v1.PolicySettings.SplittingB\x04\xe8\xc7\x31\x01\x12\x61\n\x16vm_snapshot_reattempts\x18\x08 \x01(\x0b\x32;.yandex.cloud.backup.v1.PolicySettings.RetriesConfigurationB\x04\xe8\xc7\x31\x01\x12Y\n\x03vss\x18\t \x01(\x0b\x32\x46.yandex.cloud.backup.v1.PolicySettings.VolumeShadowCopyServiceSettingsB\x04\xe8\xc7\x31\x01\x12I\n\x07\x61rchive\x18\n \x01(\x0b\x32\x38.yandex.cloud.backup.v1.PolicySettings.ArchiveProperties\x12Z\n\x12performance_window\x18\x0b \x01(\x0b\x32\x38.yandex.cloud.backup.v1.PolicySettings.PerformanceWindowB\x04\xe8\xc7\x31\x01\x12I\n\tretention\x18\x0c \x01(\x0b\x32\x30.yandex.cloud.backup.v1.PolicySettings.RetentionB\x04\xe8\xc7\x31\x01\x12K\n\nscheduling\x18\x0f \x01(\x0b\x32\x31.yandex.cloud.backup.v1.PolicySettings.SchedulingB\x04\xe8\xc7\x31\x01\x12N\n\x03\x63\x62t\x18\x10 \x01(\x0e\x32;.yandex.cloud.backup.v1.PolicySettings.ChangedBlockTrackingB\x04\xe8\xc7\x31\x01\x12\x1b\n\x13\x66\x61st_backup_enabled\x18\x11 \x01(\x08\x12$\n\x1cquiesce_snapshotting_enabled\x18\x12 \x01(\x08\x1a\xcf\x01\n\x08Interval\x12H\n\x04type\x18\x01 \x01(\x0e\x32\x34.yandex.cloud.backup.v1.PolicySettings.Interval.TypeB\x04\xe8\xc7\x31\x01\x12\x15\n\x05\x63ount\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"b\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SECONDS\x10\x01\x12\x0b\n\x07MINUTES\x10\x02\x12\t\n\x05HOURS\x10\x03\x12\x08\n\x04\x44\x41YS\x10\x04\x12\t\n\x05WEEKS\x10\x05\x12\n\n\x06MONTHS\x10\x06\x1a\x8e\x01\n\x14RetriesConfiguration\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12G\n\x08interval\x18\x02 \x01(\x0b\x32/.yandex.cloud.backup.v1.PolicySettings.IntervalB\x04\xe8\xc7\x31\x01\x12\x1c\n\x0cmax_attempts\x18\x03 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x1a\x19\n\tSplitting\x12\x0c\n\x04size\x18\x01 \x01(\x03\x1a\xf2\x01\n\x1fVolumeShadowCopyServiceSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12j\n\x08provider\x18\x02 \x01(\x0e\x32R.yandex.cloud.backup.v1.PolicySettings.VolumeShadowCopyServiceSettings.VSSProviderB\x04\xe8\xc7\x31\x01\"R\n\x0bVSSProvider\x12\x1c\n\x18VSS_PROVIDER_UNSPECIFIED\x10\x00\x12\n\n\x06NATIVE\x10\x01\x12\x19\n\x15TARGET_SYSTEM_DEFINED\x10\x02\x1a!\n\x11\x41rchiveProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a$\n\x11PerformanceWindow\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x1a)\n\tTimeOfDay\x12\x0c\n\x04hour\x18\x01 \x01(\x03\x12\x0e\n\x06minute\x18\x02 \x01(\x03\x1a\xb8\x02\n\tRetention\x12M\n\x05rules\x18\x01 \x03(\x0b\x32>.yandex.cloud.backup.v1.PolicySettings.Retention.RetentionRule\x12\x14\n\x0c\x61\x66ter_backup\x18\x02 \x01(\x08\x1a\xc5\x01\n\rRetentionRule\x12H\n\nbackup_set\x18\x01 \x03(\x0e\x32\x34.yandex.cloud.backup.v1.PolicySettings.RepeatePeriod\x12\x42\n\x07max_age\x18\x02 \x01(\x0b\x32/.yandex.cloud.backup.v1.PolicySettings.IntervalH\x00\x12\x13\n\tmax_count\x18\x03 \x01(\x03H\x00\x42\x11\n\tcondition\x12\x04\xc0\xc1\x31\x01\x1a\xe1\n\n\nScheduling\x12X\n\x0b\x62\x61\x63kup_sets\x18\x01 \x03(\x0b\x32;.yandex.cloud.backup.v1.PolicySettings.Scheduling.BackupSetB\x06\x82\xc8\x31\x02>0\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x1c\n\x14max_parallel_backups\x18\x03 \x01(\x03\x12M\n\x0erand_max_delay\x18\x04 \x01(\x0b\x32/.yandex.cloud.backup.v1.PolicySettings.IntervalB\x04\xe8\xc7\x31\x01\x12N\n\x06scheme\x18\x05 \x01(\x0e\x32\x38.yandex.cloud.backup.v1.PolicySettings.Scheduling.SchemeB\x04\xe8\xc7\x31\x01\x12K\n\x11weekly_backup_day\x18\x06 \x01(\x0e\x32*.yandex.cloud.backup.v1.PolicySettings.DayB\x04\xe8\xc7\x31\x01\x1a\xb5\x06\n\tBackupSet\x12P\n\x04time\x18\x01 \x01(\x0b\x32@.yandex.cloud.backup.v1.PolicySettings.Scheduling.BackupSet.TimeH\x00\x12m\n\x14since_last_exec_time\x18\x02 \x01(\x0b\x32M.yandex.cloud.backup.v1.PolicySettings.Scheduling.BackupSet.SinceLastExecTimeH\x00\x1a\xfa\x03\n\x04Time\x12\x42\n\x08weekdays\x18\x01 \x03(\x0e\x32*.yandex.cloud.backup.v1.PolicySettings.DayB\x04\x90\xc8\x31\x01\x12\x43\n\trepeat_at\x18\x02 \x03(\x0b\x32\x30.yandex.cloud.backup.v1.PolicySettings.TimeOfDay\x12\x45\n\x0crepeat_every\x18\x03 \x01(\x0b\x32/.yandex.cloud.backup.v1.PolicySettings.Interval\x12\x43\n\ttime_from\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.backup.v1.PolicySettings.TimeOfDay\x12\x41\n\x07time_to\x18\x05 \x01(\x0b\x32\x30.yandex.cloud.backup.v1.PolicySettings.TimeOfDay\x12\x17\n\tmonthdays\x18\x06 \x03(\x03\x42\x04\x90\xc8\x31\x01\x12!\n\x19include_last_day_of_month\x18\x07 \x01(\x08\x12\x14\n\x06months\x18\x08 \x03(\x03\x42\x04\x90\xc8\x31\x01\x12H\n\x04type\x18\t \x01(\x0e\x32\x34.yandex.cloud.backup.v1.PolicySettings.RepeatePeriodB\x04\xe8\xc7\x31\x01\x1aY\n\x11SinceLastExecTime\x12\x44\n\x05\x64\x65lay\x18\x01 \x01(\x0b\x32/.yandex.cloud.backup.v1.PolicySettings.IntervalB\x04\xe8\xc7\x31\x01\x42\x0f\n\x07setting\x12\x04\xc0\xc1\x31\x01\"\xa5\x01\n\x06Scheme\x12\x16\n\x12SCHEME_UNSPECIFIED\x10\x00\x12\n\n\x06SIMPLE\x10\x01\x12\x0f\n\x0b\x41LWAYS_FULL\x10\x02\x12\x16\n\x12\x41LWAYS_INCREMENTAL\x10\x03\x12\x16\n\x12WEEKLY_INCREMENTAL\x10\x04\x12!\n\x1dWEEKLY_FULL_DAILY_INCREMENTAL\x10\x05\x12\n\n\x06\x43USTOM\x10\x06\x12\x07\n\x03\x43\x44P\x10\x07\"R\n\x0b\x43ompression\x12\x1b\n\x17\x43OMPRESSION_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\x07\n\x03MAX\x10\x03\x12\x07\n\x03OFF\x10\x04\"_\n\rRepeatePeriod\x12\x1e\n\x1aREPEATE_PERIOD_UNSPECIFIED\x10\x00\x12\n\n\x06HOURLY\x10\x01\x12\t\n\x05\x44\x41ILY\x10\x02\x12\n\n\x06WEEKLY\x10\x03\x12\x0b\n\x07MONTHLY\x10\x04\"v\n\x03\x44\x61y\x12\x13\n\x0f\x44\x41Y_UNSPECIFIED\x10\x00\x12\n\n\x06MONDAY\x10\x01\x12\x0b\n\x07TUESDAY\x10\x02\x12\r\n\tWEDNESDAY\x10\x03\x12\x0c\n\x08THURSDAY\x10\x04\x12\n\n\x06\x46RIDAY\x10\x05\x12\x0c\n\x08SATURDAY\x10\x06\x12\n\n\x06SUNDAY\x10\x07\"v\n\x14\x43hangedBlockTracking\x12&\n\"CHANGED_BLOCK_TRACKING_UNSPECIFIED\x10\x00\x12\x12\n\x0eUSE_IF_ENABLED\x10\x01\x12\x12\n\x0e\x45NABLE_AND_USE\x10\x02\x12\x0e\n\nDO_NOT_USE\x10\x03J\x04\x08\r\x10\x0eJ\x04\x08\x0e\x10\x0f\"\x8b\x02\n\x11PolicyApplication\x12\x11\n\tpolicy_id\x18\x01 \x01(\t\x12\x1b\n\x13\x63ompute_instance_id\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12@\n\x06status\x18\x04 \x01(\x0e\x32\x30.yandex.cloud.backup.v1.PolicyApplication.Status\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"C\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03*J\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\x0e\n\nVERSION_11\x10\x01\x12\x0e\n\nVERSION_12\x10\x02\x12\x08\n\x04\x41UTO\x10\x03\x42_\n\x1ayandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.backup.v1.policy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backup'
  _POLICY.fields_by_name['id']._options = None
  _POLICY.fields_by_name['id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _POLICY.fields_by_name['name']._options = None
  _POLICY.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _POLICYSETTINGS_INTERVAL.fields_by_name['type']._options = None
  _POLICYSETTINGS_INTERVAL.fields_by_name['type']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_INTERVAL.fields_by_name['count']._options = None
  _POLICYSETTINGS_INTERVAL.fields_by_name['count']._serialized_options = b'\372\3071\002>0'
  _POLICYSETTINGS_RETRIESCONFIGURATION.fields_by_name['interval']._options = None
  _POLICYSETTINGS_RETRIESCONFIGURATION.fields_by_name['interval']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_RETRIESCONFIGURATION.fields_by_name['max_attempts']._options = None
  _POLICYSETTINGS_RETRIESCONFIGURATION.fields_by_name['max_attempts']._serialized_options = b'\372\3071\002>0'
  _POLICYSETTINGS_VOLUMESHADOWCOPYSERVICESETTINGS.fields_by_name['provider']._options = None
  _POLICYSETTINGS_VOLUMESHADOWCOPYSERVICESETTINGS.fields_by_name['provider']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_RETENTION_RETENTIONRULE.oneofs_by_name['condition']._options = None
  _POLICYSETTINGS_RETENTION_RETENTIONRULE.oneofs_by_name['condition']._serialized_options = b'\300\3011\001'
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['weekdays']._options = None
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['weekdays']._serialized_options = b'\220\3101\001'
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['monthdays']._options = None
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['monthdays']._serialized_options = b'\220\3101\001'
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['months']._options = None
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['months']._serialized_options = b'\220\3101\001'
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['type']._options = None
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME.fields_by_name['type']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_SINCELASTEXECTIME.fields_by_name['delay']._options = None
  _POLICYSETTINGS_SCHEDULING_BACKUPSET_SINCELASTEXECTIME.fields_by_name['delay']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_SCHEDULING_BACKUPSET.oneofs_by_name['setting']._options = None
  _POLICYSETTINGS_SCHEDULING_BACKUPSET.oneofs_by_name['setting']._serialized_options = b'\300\3011\001'
  _POLICYSETTINGS_SCHEDULING.fields_by_name['backup_sets']._options = None
  _POLICYSETTINGS_SCHEDULING.fields_by_name['backup_sets']._serialized_options = b'\202\3101\002>0'
  _POLICYSETTINGS_SCHEDULING.fields_by_name['rand_max_delay']._options = None
  _POLICYSETTINGS_SCHEDULING.fields_by_name['rand_max_delay']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_SCHEDULING.fields_by_name['scheme']._options = None
  _POLICYSETTINGS_SCHEDULING.fields_by_name['scheme']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS_SCHEDULING.fields_by_name['weekly_backup_day']._options = None
  _POLICYSETTINGS_SCHEDULING.fields_by_name['weekly_backup_day']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['compression']._options = None
  _POLICYSETTINGS.fields_by_name['compression']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['format']._options = None
  _POLICYSETTINGS.fields_by_name['format']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['reattempts']._options = None
  _POLICYSETTINGS.fields_by_name['reattempts']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['splitting']._options = None
  _POLICYSETTINGS.fields_by_name['splitting']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['vm_snapshot_reattempts']._options = None
  _POLICYSETTINGS.fields_by_name['vm_snapshot_reattempts']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['vss']._options = None
  _POLICYSETTINGS.fields_by_name['vss']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['performance_window']._options = None
  _POLICYSETTINGS.fields_by_name['performance_window']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['retention']._options = None
  _POLICYSETTINGS.fields_by_name['retention']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['scheduling']._options = None
  _POLICYSETTINGS.fields_by_name['scheduling']._serialized_options = b'\350\3071\001'
  _POLICYSETTINGS.fields_by_name['cbt']._options = None
  _POLICYSETTINGS.fields_by_name['cbt']._serialized_options = b'\350\3071\001'
  _globals['_FORMAT']._serialized_start=4606
  _globals['_FORMAT']._serialized_end=4680
  _globals['_POLICY']._serialized_start=128
  _globals['_POLICY']._serialized_end=380
  _globals['_POLICYSETTINGS']._serialized_start=383
  _globals['_POLICYSETTINGS']._serialized_end=4334
  _globals['_POLICYSETTINGS_INTERVAL']._serialized_start=1466
  _globals['_POLICYSETTINGS_INTERVAL']._serialized_end=1673
  _globals['_POLICYSETTINGS_INTERVAL_TYPE']._serialized_start=1575
  _globals['_POLICYSETTINGS_INTERVAL_TYPE']._serialized_end=1673
  _globals['_POLICYSETTINGS_RETRIESCONFIGURATION']._serialized_start=1676
  _globals['_POLICYSETTINGS_RETRIESCONFIGURATION']._serialized_end=1818
  _globals['_POLICYSETTINGS_SPLITTING']._serialized_start=1820
  _globals['_POLICYSETTINGS_SPLITTING']._serialized_end=1845
  _globals['_POLICYSETTINGS_VOLUMESHADOWCOPYSERVICESETTINGS']._serialized_start=1848
  _globals['_POLICYSETTINGS_VOLUMESHADOWCOPYSERVICESETTINGS']._serialized_end=2090
  _globals['_POLICYSETTINGS_VOLUMESHADOWCOPYSERVICESETTINGS_VSSPROVIDER']._serialized_start=2008
  _globals['_POLICYSETTINGS_VOLUMESHADOWCOPYSERVICESETTINGS_VSSPROVIDER']._serialized_end=2090
  _globals['_POLICYSETTINGS_ARCHIVEPROPERTIES']._serialized_start=2092
  _globals['_POLICYSETTINGS_ARCHIVEPROPERTIES']._serialized_end=2125
  _globals['_POLICYSETTINGS_PERFORMANCEWINDOW']._serialized_start=2127
  _globals['_POLICYSETTINGS_PERFORMANCEWINDOW']._serialized_end=2163
  _globals['_POLICYSETTINGS_TIMEOFDAY']._serialized_start=2165
  _globals['_POLICYSETTINGS_TIMEOFDAY']._serialized_end=2206
  _globals['_POLICYSETTINGS_RETENTION']._serialized_start=2209
  _globals['_POLICYSETTINGS_RETENTION']._serialized_end=2521
  _globals['_POLICYSETTINGS_RETENTION_RETENTIONRULE']._serialized_start=2324
  _globals['_POLICYSETTINGS_RETENTION_RETENTIONRULE']._serialized_end=2521
  _globals['_POLICYSETTINGS_SCHEDULING']._serialized_start=2524
  _globals['_POLICYSETTINGS_SCHEDULING']._serialized_end=3901
  _globals['_POLICYSETTINGS_SCHEDULING_BACKUPSET']._serialized_start=2912
  _globals['_POLICYSETTINGS_SCHEDULING_BACKUPSET']._serialized_end=3733
  _globals['_POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME']._serialized_start=3119
  _globals['_POLICYSETTINGS_SCHEDULING_BACKUPSET_TIME']._serialized_end=3625
  _globals['_POLICYSETTINGS_SCHEDULING_BACKUPSET_SINCELASTEXECTIME']._serialized_start=3627
  _globals['_POLICYSETTINGS_SCHEDULING_BACKUPSET_SINCELASTEXECTIME']._serialized_end=3716
  _globals['_POLICYSETTINGS_SCHEDULING_SCHEME']._serialized_start=3736
  _globals['_POLICYSETTINGS_SCHEDULING_SCHEME']._serialized_end=3901
  _globals['_POLICYSETTINGS_COMPRESSION']._serialized_start=3903
  _globals['_POLICYSETTINGS_COMPRESSION']._serialized_end=3985
  _globals['_POLICYSETTINGS_REPEATEPERIOD']._serialized_start=3987
  _globals['_POLICYSETTINGS_REPEATEPERIOD']._serialized_end=4082
  _globals['_POLICYSETTINGS_DAY']._serialized_start=4084
  _globals['_POLICYSETTINGS_DAY']._serialized_end=4202
  _globals['_POLICYSETTINGS_CHANGEDBLOCKTRACKING']._serialized_start=4204
  _globals['_POLICYSETTINGS_CHANGEDBLOCKTRACKING']._serialized_end=4322
  _globals['_POLICYAPPLICATION']._serialized_start=4337
  _globals['_POLICYAPPLICATION']._serialized_end=4604
  _globals['_POLICYAPPLICATION_STATUS']._serialized_start=4537
  _globals['_POLICYAPPLICATION_STATUS']._serialized_end=4604
# @@protoc_insertion_point(module_scope)