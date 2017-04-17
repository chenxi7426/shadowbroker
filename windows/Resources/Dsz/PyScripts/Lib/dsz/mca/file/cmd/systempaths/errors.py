# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 1
ERR_GETSYSDIR_FAILED = mcl.status.framework.ERR_START + 2
ERR_GETWINDIR_FAILED = mcl.status.framework.ERR_START + 3
ERR_GETTEMPDIR_FAILED = mcl.status.framework.ERR_START + 4
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_GETSYSDIR_FAILED: 'Failed to retrieve system directory',
   ERR_GETWINDIR_FAILED: 'Failed to retrieve windows directory',
   ERR_GETTEMPDIR_FAILED: 'Failed to retrieve temp directory'
   }