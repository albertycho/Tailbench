/* DO NOT MODIFY --- generated by ../../tools/logdef.pl from logdef.dat 
                     on Wed Sep  1 18:45:13 2021

<std-header orig-src='shore' genfile='true'>

SHORE -- Scalable Heterogeneous Object REpository

Copyright (c) 1994-99 Computer Sciences Department, University of
                      Wisconsin -- Madison
All Rights Reserved.

Permission to use, copy, modify and distribute this software and its
documentation is hereby granted, provided that both the copyright
notice and this permission notice appear in all copies of the
software, derivative works or modified versions, and any portions
thereof, and that both notices appear in supporting documentation.

THE AUTHORS AND THE COMPUTER SCIENCES DEPARTMENT OF THE UNIVERSITY
OF WISCONSIN - MADISON ALLOW FREE USE OF THIS SOFTWARE IN ITS
"AS IS" CONDITION, AND THEY DISCLAIM ANY LIABILITY OF ANY KIND
FOR ANY DAMAGES WHATSOEVER RESULTING FROM THE USE OF THIS SOFTWARE.

This software was developed with support by the Advanced Research
Project Agency, ARPA order number 018 (formerly 8230), monitored by
the U.S. Army Research Laboratory under contract DAAB07-91-C-Q518.
Further funding for this work was provided by DARPA through
Rome Research Laboratory Contract No. F30602-97-2-0247.

*/

#include "w_defines.h"

/*  -- do not edit anything above this line --   </std-header>*/


enum kind_t { 
	t_comment = 0,
	t_compensate = 1,
	t_skip = 2,
	t_chkpt_begin = 3,
	t_chkpt_bf_tab = 4,
	t_chkpt_xct_tab = 5,
	t_chkpt_dev_tab = 6,
	t_chkpt_end = 7,
	t_mount_vol = 8,
	t_dismount_vol = 9,
	t_xct_abort = 10,
	t_xct_freeing_space = 11,
	t_xct_end = 12,
	t_xct_prepare_st = 13,
	t_xct_prepare_lk = 14,
	t_xct_prepare_alk = 15,
	t_xct_prepare_stores = 16,
	t_xct_prepare_fi = 17,
	t_alloc_file_page = 18,
	t_alloc_pages_in_ext = 19,
	t_free_pages_in_ext = 20,
	t_create_ext_list = 21,
	t_free_ext_list = 22,
	t_set_ext_next = 23,
	t_store_operation = 24,
	t_page_link = 25,
	t_page_insert = 26,
	t_page_remove = 27,
	t_page_format = 28,
	t_page_mark = 29,
	t_page_reclaim = 30,
	t_page_shift = 31,
	t_page_splice = 32,
	t_page_splicez = 33,
	t_page_set_byte = 34,
	t_page_image = 35,
	t_btree_purge = 36,
	t_btree_insert = 37,
	t_btree_remove = 38,
	t_rtree_insert = 39,
	t_rtree_remove = 40,
	t_max_logrec = 41
};
