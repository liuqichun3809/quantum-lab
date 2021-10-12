class DABoard_Defines:
   'Class which contains all #defines from uhwd_common.h'
   def __init__(self):
      print ("Calling Board_Defines class constructor")
      
   DRAM_SIZE_BYTES           = 0x40000   
   CMD_NON_VAL               = 0x0       
   CMD_READ_REG              = 0x1       
   CMD_WRITE_REG             = 0x2       
   CMD_READ_MEM              = 0x3       
   CMD_WRITE_MEM             = 0x4       
   CMD_CTRL_CMD              = 0x5       
   CMD_LAST                  = CMD_CTRL_CMD
   CTRL_NON_VAL              = 0x0       
   CTRL_REINIT               = 0x1       
   CTRL_START_CAP            = 0x2       
   CTRL_CHECK_CAP            = 0x3       
   CTRL_START_PLAY           = 0x4       
   CTRL_STOP_PLAY            = 0x5       
   CTRL_ERASE_ALL            = 0x6
   CTRL_ERASE_PART           = 0x7
   CTRL_SET_WDTO             = 0x8
   CTRL_SET_LOOP             = 0x9       
   CTRL_FILL_MEM             = 0xA   
   CTRL_DUMP_MEM             = 0xB       
   CTRL_READ_FLAG            = 0xF
   CTRL_INIT                 = 0x1A
   CTRL_RD_DAC1              = 0x1C
   CTRL_RD_DAC2              = 0x1D
   CTRL_SYNC_CTRL            = 0x18
   CTRL_DAC_POWER            = 0x1E
   CTRL_DAC_DEFAULT          = 0x1B
   CTRL_DUMP_DMARXREGS       = 0x12      
   CTRL_MONITOR              = 0x13
   CTRL_CMD_ADPT             = 0x21
   CTRL_JESD_DATA_IF_SY_STAT = 0x22
   CTRL_UPDATE_DELAYIP_REG   = 0x23
   CTRL_DATA_AQUIRE          = 0x24
   CTRL_DATA_AWGCORE         = 0x25
   CTRL_DATA_SPI             = 0x26
   CTRL_LAST                 = CTRL_DATA_AWGCORE
   STAT_SUCCESS              = 0x0       
   STAT_ERROR                = 0x1       
   STAT_CMDERR               = 0x2       
   STAT_RDERR                = 0x3       
   STAT_WRERR                = 0x4       
   STAT_MEM_RANGE_ERR        = 0x5       
   STAT_MEM_ALIGN_ERR        = 0x6       
   STAT_SIZE_ERR             = 0x7       
   STAT_SIZE_ALIGN_ERR       = 0x8       
   STAT_ADDR_ALIGN_ERR       = 0x9       
   STAT_DATAIF_BUSY          = 0xA       
   STAT_DATAIF_ERR           = 0xB       
   STAT_DMA_ERR              = 0xC       
   STAT_LAST                 = STAT_DMA_ERR
   REGREG_NON_VAL = 0x00
   REG_IDNTITY = 0x00
   REG_VERSION = 0x04
   REG_SY_STAT = 0x08
   REG_TESTREG = 0x0C
   REG_CNFG_REG0 = 0x40
   REG_CNFG_REG1 = 0x44
   REG_CNFG_REG5 = 0x114
   REG_CTRL_REG = 0xC0
   REG_STATUS_1 = 0x100
   REG_STATUS_2 = 0x104
   REG_LAST = REG_STATUS_2
   CTRL_CH1_RUN = 0
   CTRL_CH2_RUN = 1
   CTRL_CH1_STOP = 4
   CTRL_CH2_STOP = 5

   CNFG4_CH1_CMD_CS = 0
   CNFG4_CH2_CMD_CS = 1
   CNFG4_CH1_WAV_CS = 4
   CNFG4_CH2_WAV_CS = 5
   CNFG4_CH1_RD_BACK = 8
   CNFG4_CH2_RD_BACK = 9