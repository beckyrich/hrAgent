from enum import Enum

class JobTypeEnum(str, Enum):
    seasonal = 'seasonal'
    fte = 'fte'
    part_time = 'part_time'
    ten_99 = 'ten_99'
    agency = 'agency'
    contract_to_hire = 'contract_to_hire'

class JobLevelEnum(str, Enum):
    entry = 'entry'
    mid = 'mid'
    senior = 'senior'
    principal = 'principal'
    management = 'management'
    executive = 'executive'
