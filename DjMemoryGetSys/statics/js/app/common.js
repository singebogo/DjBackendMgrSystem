// -----------------------------boostarp table 双击域 --------------------------------------------------------------
// 初始化双击域

function initDbSelect(url, $target) {

    $('#dbselecttable').bootstrapTable("destroy");
    var columns = [{
        field: 'Id',
        title: 'Id',
        formatter: function (value, row, index) {
            return index + 1;
        },
    }, {
        field: 'pk',
        title: 'code'
    }, {
        field: 'fields.codename',
        title: 'name'
    }];

    $('#dbselecttable').bootstrapTable({
        url: url,        // 表格数据来源
        method: 'POST',                      //请求方式（*）
        ajaxOptions: {
            headers: {
                // "Access-Control-Allow-Origin": '*',
                "X-CSRFToken": "qq",
                "contentType": "application/x-www-form-urlencoded",
            }
        },
        toolbar: '#toolbar',                //工具按钮用哪个容器
        striped: true,                      //是否显示行间隔色
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true,                   //是否显示分页（*）
        sortable: true,                    //是否启用排序
        sortOrder: "asc",                   //排序方式
        sidePagination: "client",           //分页方式：client客户端分页，server服务端分页（*）
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 5,                       //每页的记录行数（*）
        pageList: [5],                      //可供选择的页的行数（*）
        search: false,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        strictSearch: false,
        showColumns: false,                  //是否显示所有的列
        showRefresh: false,                  //是否显示刷新按钮
        minimumCountColumns: 2,             //最少允许的列数
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "Id",                     //每一行的唯一标识，一般为主键列
        showToggle: false,                    //是否显示详细视图和列表视图的切换按钮
        cardView: false,                    //是否显示详细视图
        detailView: false,                   //是否显示父子表
        queryParams: queryParamsFun(),
        columns: columns,
        onClickRow: function (data, $element, field) {
            $target.val(data['pk']);
            // 关闭
            $('#dbSelectModal').css({display: 'none'});
            $('#dbselectfade').css({display: 'none'});
        },
    });

    function queryParamsFun(params) {
        //这里的键的名字和控制器的变量名必须一致，这边改动，控制器也需要改成一样的
        var temp = {
            selectCode: $('#selectCode').val(),
            selectName: $('#selectName').val(),
        };
        return temp;
    };

    $('#dbSelectQuery').click(function () {
        $("#dbselecttable").bootstrapTable('refreshOptions', {pageNumber: 1, queryParams: queryParamsFun()});
    });

    $('#dbSelectCancel').click(function () {
        $('#selectCode').val("");
        $('#selectName').val("");
    });

    $('#dbSelectReset').click(function () {
        $('#selectCode').val("");
        $('#selectName').val("");
    });
};

// -------------------------------------------数据导入展示模块-----------------------------------------------------------------------

function fileImportDialogHtml() {
    var dialogHtml = '<div id="fileImportFade" class="black_overlay">\
    </div><div class="white_content_fileImport" id="fileImportModal" tabindex="-1" role="dialog" aria-labelledby="fileImportModal"> \
    <div id="fileImportModalDialog" class="fileImportmodalDialog" role="document"> \
        <div class="modal-content"> \
            <div class="modal-header"> \
                <div class="row"> \
                    <div class="col-xs-3"> \
                        <span id="title">数据批量导入 </span> \
                    </div> \
                    <div class="col-xs-offset-11 col-xs-1" style="margin-left: 96%;"> \
                        <a href="javascript:void(0)" id="fileImportclose"> \
                            <i class="glyphicon glyphicon-remove"></i> \
                        </a> \
                    </div> \
                </div> \
            </div> \
            <div class="modal-body"> \
                <form class="form-horizontal" role="form"> \
                    <div class="row"> \
                        <div class="col-xs-12"> \
                            <div class="col-lg-6 col-md-6 col-xs-6"> \
                                <div class="form-group"> \
                                    <label for="wechatImport" class="col-lg-5 col-md-5 col-xs-5 control-label">微信账单导入</label> \
                                    <div class="col-lg-7 col-md-7 col-xs-7"> \
                                        <input type="file" class="form-control input-sm" id="wechatImport" \
                                            placeholder="请输入"> \
                                    </div> \
                                </div> \
                            </div> \
                            <div class="col-lg-6 col-md-6 col-xs-6"> \
                                <div class="form-group"> \
                                    <label for="ailplayImport" \
                                        class="col-lg-5 col-md-5 col-xs-5 control-label">支付宝账单导入</label> \
                                    <div class="col-lg-7 col-md-7 col-xs-7"> \
                                        <input type="file" class="form-control input-sm" id="ailplayImport" \
                                            placeholder="请输入"> \
                                    </div> \
                                </div> \
                            </div> \
                            <div class="clearfix"></div> \
                        </div> \
                        <div class="col-xs-12"> \
                            <table id="fileImportTable"></table> \
                            <div class="clearfix"></div> \
                        </div> \
                    </div> \
                </form> \
            </div> \
            <div class="modal-footer"> \
                <div class="row"> \
                <div class="col-xs-10"> \
                    <div id ="fileImportPoptips" style="float:left;color:red;"></div> \
                </div> \
                <div class="col-lg-7 col-md-7 col-xs-7"> \
                    <div class="form-group"> \
                        <input type="button" class= \'btn btn-primary btn-xs\' id=\'fileImport\' value="提交" /> \
                        <input type="button" class= \'btn btn-primary btn-xs\' id=\'fileImportReset\' value="重置" /> \
                        <input type="button" class= \'btn btn-primary btn-xs\' id=\'fileImportCancel\' value="取消" \
                            onclick="$(\'#fileImportModal\').css({display:\'none\'});$(\'#fileImportFade\').css({display:\'none\'});"/> \
                    </div> \
                </div> \
                </div> \
            </div> \
        </div> \
    </div> \
</div> ';
    return dialogHtml;
};

// 初始化账单导入

function initFileImportTable(columns, data) {

    $('#fileImportTable').bootstrapTable("destroy");

    $('#fileImportTable').bootstrapTable({
        data: data,
        toolbar: '#toolbar',                //工具按钮用哪个容器
        striped: true,                      //是否显示行间隔色
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true,                   //是否显示分页（*）
        sortable: true,                    //是否启用排序
        sortOrder: "asc",                   //排序方式
        sidePagination: "client",           //分页方式：client客户端分页，server服务端分页（*）
        pageNumber: 1,                       //初始化加载第一页，默认第一页
        pageSize: 10,                       //每页的记录行数（*）
        pageList: [10, 30, 50],                      //可供选择的每页的行数（*）
        search: false,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        strictSearch: false,
        showColumns: false,                  //是否显示所有的列
        showRefresh: false,                  //是否显示刷新按钮
        minimumCountColumns: 2,             //最少允许的列数
        clickToSelect: true,                //是否启用点击选中行
        uniqueId: "Id",                     //每一行的唯一标识，一般为主键列
        idField: "Id",
        showToggle: false,                    //是否显示详细视图和列表视图的切换按钮
        cardView: false,                    //是否显示详细视图
        detailView: false,                   //是否显示父子表
        columns: columns,
    });

    $('#fileImport').click(function () {
        // let options=$("#fileImportTable").bootstrapTable('getOptions');
        // let columnsArray=options.columns[0];
        // let columns = [];
        // for(let i = 0; i < columnsArray.length; i++){
        //     if("操作".localeCompare(columnsArray[i].title) == 0){
        //         continue;
        //     }
        //     field = columnsArray[i].field;
        //     title = columnsArray[i].title;
        //     columns.push({field: field, title:title});
        // } 

        if (($('#wechatImport').val()).length == 0 && ($('#ailplayImport').val()).length == 0) {
            $('#fileImportPoptips').text("未选择要导入的文件!");
            return;
        }

        let dataLists = $("#fileImportTable").bootstrapTable('getData');
        // requried 
        let requriedArray = [];
        if (dataLists[0][9].localeCompare("支付宝") == 0) {
            for (let i = 0; i < dataLists.length; i++) {
                if (dataLists[i][13].length == 0 || dataLists[i][13].localeCompare('null') == 0) {
                    requriedArray.push(i);
                }
            }
        } else {
            for (let i = 0; i < dataLists.length; i++) {
                if (dataLists[i][12].length == 0 || dataLists[i][12].localeCompare('null') == 0) {
                    requriedArray.push(i);
                }
            }
        }
        if (requriedArray.length > 0) {
            $('#fileImportPoptips').text(("ID: " + JSON.stringify(requriedArray) + " 列为[科目]必填!!!"));
            return;
        }
        // 0   		2   	3   	-1  	-1 		    9   	8    	5    	微信    			1   			10    11   12
        // 4  		5  	    3        0  	 1   		2      -1  		6+7     9     			   0    	    	11    12   13    
        // 交易时间,交易对方,商品名称,账务流水号,业务流水号,商户订单号,交易单号,金额(元),交易渠道(支付宝/微信),业务类型(转账，其他),备注,消费人,科目
        let datasArray = [];
        creatorcode = '1';
        createtime = getDate();
        vaildid = '1';

        if (dataLists[0][9].localeCompare("支付宝") == 0) {
            let aliPlayArray = [4, 5, 3, 0, 1, 2, -1, "money", 9, 10, 11, 12, 13];
            for (let i = 0; i < dataLists.length; i++) {
                let dataArray = [];
                for (let j = 0; j < aliPlayArray.length; j++) {
                    if ("money".localeCompare(aliPlayArray[j]) == 0) {
                        dataArray.push(Math.abs(parseFloat(dataLists[i][6]) + parseFloat(dataLists[i][7])));
                    } else if (aliPlayArray[j] == -1) {
                        dataArray.push("");
                    } else {
                        dataArray.push(dataLists[i][aliPlayArray[j]]);
                    }
                }
                dataArray.push(creatorcode);
                dataArray.push(createtime);
                dataArray.push(vaildid);
                datasArray.push(dataArray);
            }
        } else {
            let wechatArray = [0, 2, 3, -1, -1, 9, 8, 5, "channel", 1, 10, 11, 12];
            for (let i = 0; i < dataLists.length; i++) {
                let dataArray = [];
                for (let j = 0; j < wechatArray.length; j++) {
                    if ("channel".localeCompare(wechatArray[j]) == 0) {
                        dataArray.push("微信");
                    } else if (wechatArray[j] == -1) {
                        dataArray.push("");
                    } else {
                        dataArray.push(dataLists[i][wechatArray[j]]);
                    }
                }
                dataArray.push(creatorcode);
                dataArray.push(createtime);
                dataArray.push(vaildid);
                datasArray.push(dataArray);
            }
        }
        // let data = {columns:JSON.stringify(columns), data: JSON.stringify(dataLists)};

        let data = {data: JSON.stringify(datasArray)};
        $.ajax({
            url: "http://127.0.0.1:8000/DailyInout/blukCreate/",
            type: 'POST',
            data: data,
            traditional: true,//这里设置为true
            // 上面data为提交数据，下面data形参指代的就是异步提交的返回结果data
            success: function (obj) {
                data = JSON.parse(obj);
                if ("1".localeCompare(data['code']) == 0) {
                    notices(data['msg']);
                    $('#wechatImport').val("");
                    $('#ailplayImport').val("");
                    $('#fileImportTable').bootstrapTable("destroy");

                    $('#fileImportModal').css({display: "none"});
                    $('#fileImportFade').css({display: "none"});
                } else {
                    $('#fileImportPoptips').text("");
                    $('#fileImportPoptips').text(data['msg']);
                }
            },
            error: function (obj) {
                $('#fileImportPoptips').text("");
                $('#fileImportPoptips').text(obj);
            }
        });

    });

    $('#fileImportCancel').click(function () {
        $('#wechatImport').val("");
        $('#ailplayImport').val("");
        $('#fileImportTable').bootstrapTable("destroy");
        $('#fileImportPoptips').text("");
    });
    $('#fileImportclose').click(function () {
        $('#wechatImport').val("");
        $('#ailplayImport').val("");
        $('#fileImportTable').bootstrapTable("destroy");

        $('#fileImportModal').css({display: "none"});
        $('#fileImportFade').css({display: "none"});
        $('#fileImportPoptips').text("");
    });

    $('#fileImportReset').click(function () {
        $('#wechatImport').val("");
        $('#ailplayImport').val("");
        $('#fileImportTable').bootstrapTable("destroy");
        $('#fileImportPoptips').text("");
    });
};

function FileImportDeleteByIds(that) {
    var uniqueId = that.parentNode.parentNode.getAttribute('data-uniqueid');
    $('#fileImportTable').bootstrapTable('removeByUniqueId', parseInt(uniqueId));
};


// -----------------------------boostarp table 结果表格 --------------------------------------------------------------
var maxLimit;
var minLimit;

//初始化bootstrap-table的内容
function initResultTable(queryUrl, deleteurl, method, columns, uniqueId, dialogbodyObj, queryParamsFun, onLoadSuccessFun, onLoadErrorFun) {
    //记录页面bootstrap-table全局变量$table，方便应用
    $table = $('#table').bootstrapTable({
        url: queryUrl,                      //请求后台的URL（*）
        method: method,                      //请求方式（*）
        toolbar: '#toolbar',              //工具按钮用哪个容器
        contentType: "application/x-www-form-urlencoded",      // post请求必须要有，否则后台接受不到参数
        // ajaxOptions: {
        //     headers: { "Access-Control-Allow-Origin": '*' }
        // },
        clickToSelect: true,                                   // 是否点击选中行
        striped: true,                      //是否显示行间隔色
        cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true,                   //是否显示分页（*）
        sortable: true,                     //是否启用排序
        sortOrder: "asc",                   //排序方式
        sidePagination: "client",           //分页方式：client客户端分页，server服务端分页（*）
        pageNumber: 1,                      //初始化加载第一页，默认第一页,并记录
        pageSize: 15,                       //每页的记录行数（*）
        pageList: [15, 30, 50, 100],        //可供选择的每页的行数（*）
        search: false,                      //是否显示表格搜索
        strictSearch: true,
        showColumns: true,                  //是否显示所有的列（选择显示的列）
        showRefresh: true,                  //是否显示刷新按钮
        minimumCountColumns: 2,             //最少允许的列数
        clickToSelect: true,                //是否启用点击选中行
        // height: 650,                      //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
        uniqueId: uniqueId,                     //每一行的唯一标识，一般为主键列
        showToggle: true,                   //是否显示详细视图和列表视图的切换按钮
        showFooter: true,
        showHeader: true,
        showColumns: true,
        showPaginationSwitch: true,         // True to show the pagination switch button.
        cardView: false,                    //是否显示详细视图
        detailView: false,                  //是否显示父子表
        singleSelect: true,                 // 单选checkbox 
        //得到查询的参数
        queryParams: queryParamsFun(),
        columns: columns,

        onLoadSuccess: onLoadSuccessFun,
        onLoadError: onLoadErrorFun,
    });

    // 查询按钮
    $('#query').click(function () {
        $("#table").bootstrapTable('refreshOptions', {pageNumber: 1, queryParams: queryParamsFun()});
    });

    function change(title, style, bVisiblePk = false) {
        // 	返回所选的行，当没有选择任何行的时候返回一个空数组。
        var seles = $('#table').bootstrapTable('getSelections');
        if (seles.length > 1) {
            notices("警告！只能选择一条数据...");
            return;
        } else if (seles.length == 0) {
            notices("警告！请选择一条数据...");
            return;
        }
        // 修改页面
        // 初始化
        $('#popoveModal').css({display: "block"});
        $('#fade').css({display: "block"});

        $('#title').text(title);

        let tags = $('#popoveModalDialog .modal-body .form-horizontal .form-group div').children();

        $.each(tags, function (i, item) {
            $(item).removeAttr("disabled");
        });
        var row = $('#table').bootstrapTable('getSelections');

        for (let i = 0; i < dialogbodyObj.length; i++) {
            id = dialogbodyObj[i].id;
            value = row[0][id];
            $('#' + id).val(value);

            if (dialogbodyObj[i].pk) {
                $('#' + id).attr("disabled", "disabled");
                if (!bVisiblePk) {
                    $('#' + id).val("");
                }
            }
            if (dialogbodyObj[i].readonly) {
                $('#' + id).attr("readonly", "true");
            }
            if (dialogbodyObj[i].display) {
                $($('#' + dialogbodyObj[i].id).parent().parent().parent()).css({display: style});
            }
        }
        ;
    }

    $('#copy').click(function () {
        change("复制配置", 'none');
    });

    $('#change').click(function () {
        change("修改配置", 'block', bVisiblePk = true);
    });

    $('#delete').click(function () {
        // 删除
        var row = $('#table').bootstrapTable('getSelections');
        if (row.length > 1) {
            notices("警告！只能选择一条数据...");
            return;
        } else if (row.length == 0) {
            notices("警告！请选择一条数据...");
            return;
        }
        confirm(function (pk) {
            $.ajax({
                url: deleteurl, //也可以反向解析{% url 'login' %}
                type: 'POST',
                data: {'pk': pk},
                // 上面data为提交数据，下面data形参指代的就是异步提交的返回结果data
                success: function (obj) {
                    data = JSON.parse(obj);
                    if ("1".localeCompare(data['code']) == 0) {
                        notices(data['msg']);
                        $('#table').bootstrapTable('removeByUniqueId', pk);
                    } else {
                        notices(data['msg']);
                    }
                },
                error: function (obj) {
                    notices(obj);
                }
            });
        }, row[0][uniqueId]);
    });

    // 查看
    $('#table').on('click', 'a', function (e) {
        $target = $(e.target);
        row = $target.attr("row");
        $('#popoveModal').css({display: "block"});
        $('#fade').css({display: "block"});

        $('#title').text("查看配置");

        // disabled 
        $('#sure').css("visibility", "hidden");
        $('#cancel').css("visibility", "hidden");

        let tags = $('#popoveModalDialog .modal-body .form-horizontal .form-group div').children();

        // 数据展示
        row = JSON.parse(row);
        for (let i = 0; i < dialogbodyObj.length; i++) {
            id = dialogbodyObj[i].id;
            $('#' + id).val(row[id]);

            if (dialogbodyObj[i].display) {
                $($('#' + dialogbodyObj[i].id).parent().parent().parent()).css({display: "block"});
            }
        }
        ;

        $.each(tags, function (i, item) {
            $(item).attr("disabled", "disabled");
        });
    });
};


// -----------------------------boostarp table columns format--------------------------------------------------------------

function linkFormatter(value, row, index) {

    function replacer(key, value) {
        if (key.localeCompare('codecodes') == 0 || key.localeCompare('remark') == 0) {
            // replace backspace
            if (value.indexOf(' ') != -1) {
                value = value.replace(/\s/g, "&nbsp;");
            }
        }
        return value;
    }

    row = JSON.stringify(row, replacer);
    let html = '<a href=\'javascript:void(0)\' row=' + row + ' title=\'单击打开连接\'>' + value + '</a>';
    return html;
}

function ellipsisFormater(value, row, index) {
    if (value && value.length > 11) {
        value = value.slice(0, 11) + "....";
    }
    return value;
}

//Email字段格式化
function emailFormatter(value, row, index) {
    return "<a href='mailto:" + value + "' title='单击打开连接'>" + value + "</a>";
}

//性别字段格式化
function sexFormatter(value) {
    if (value == "女") {
        color = 'Red';
    } else if (value == "男") {
        color = 'Green';
    } else {
        color = 'Yellow';
    }
    return '<div  style="color: ' + color + '">' + value + '</div>';
}

//操作栏的格式化
function actionFormatter(value, row, index) {
    var id = value;
    var result = "";
    result += "<a href='javascript:;' class='btn btn-xs green' onclick=\"EditViewById('" + id + "', view='view')\" title='查看'><span class='glyphicon glyphicon-search'></span></a>";
    result += "<a href='javascript:;' class='btn btn-xs blue' onclick=\"EditViewById('" + id + "')\" title='编辑'><span class='glyphicon glyphicon-pencil'></span></a>";
    result += "<a href='javascript:;' class='btn btn-xs red' onclick=\"DeleteByIds('" + id + "')\" title='删除'><span class='glyphicon glyphicon-remove'></span></a>";
    return result;
}

var MetricsNotices;

function getMetricsNotices() {
    // get notices info
    $.ajax({
        url: 'http://127.0.0.1:8000/Metrics/limitTypeMetrics/',
        type: 'POST',
        data: {limittype: "0"},
        success: function (obj) {
            MetricsNotices = JSON.parse(obj);
        },
        error: function (obj) {
            notices(obj);
        }
    });
}

function sumFormatter(value, ele, row, col) {
    // 支出
    if ('out'.localeCompare(ele['codecodes__codetype']) == 0) {
        ele.sum = -Math.abs(ele.sum);

    }
    let color = FormatNotices(ele, "1", ele.sum);
    return '<div><span style="' + color + '">' + ele.sum + '</span></div>';
}

//计算此列的值
function feetFormatter(rows) {
    var total = 0;
    for (var i = 0; i < rows.length; i++) {
        total += parseFloat(rows[i].sum);
    }
    return total.toFixed(2);
}


//字段格式化
function colorFormatter(value, ele, row, col) {
    if (!value) {
        return '<div style="color: black">' + " - " + '</div>';
    }
    let color = FormatNotices(ele, "0", value);
    // value 值
    // ele 字典
    // index 索引

    return '<a data-container="body" data-toggle="popover" data-placement="top" data-html=true '
        + 'style="' + color + ';"'
        + 'href="javascript:void(0)" ele=' + JSON.stringify(ele) + ' row=' + row + ' col=' + col + '>'
        + value
        + '</a>';
}

// 获取预警配置并设置预警信息
function FormatNotices(ele, sumlimittype, value) {
    color = 'color: black';

    if (MetricsNotices && ele.codecodes in MetricsNotices) {
        let Metricsobj = JSON.parse(MetricsNotices[ele.codecodes]);
        if (sumlimittype in Metricsobj && Metricsobj[sumlimittype]) {
            let dayMetricsobj = JSON.parse(Metricsobj[sumlimittype]);

            let minLimit, maxLimit;
            let minLimitStyle, maxLimitStyle = color;

            if (dayMetricsobj.length != 0) {
                if (dayMetricsobj[1]) {
                    minLimit = dayMetricsobj[1].limit;
                    minLimitStyle = dayMetricsobj[1].style;
                }
                if (dayMetricsobj[0]) {
                    maxLimit = dayMetricsobj[0].limit;
                    maxLimitStyle = dayMetricsobj[0].style;
                }
                if (maxLimit) {
                    if (Math.abs(value) > maxLimit) {
                        color = maxLimitStyle;
                    }
                }
                if (minLimit) {
                    if (minLimit < Math.abs(value) && Math.abs(value) < maxLimit) {
                        color = minLimitStyle;
                    }
                }
            }
        }
    }
    return color;
}

// ----------------------------时间相关--------------------------------------------------------------

function getDate() {
    var mydate = new Date();
    var str = "" + mydate.getFullYear() + "-";
    str += ("0" + (mydate.getMonth() + 1)).slice(-2) + "-";
    str += ("0" + (mydate.getDate())).slice(-2);
    return str;
};

function getMonth() {
    var mydate = new Date();
    var str = "" + mydate.getFullYear() + "-";
    str += ("0" + (mydate.getMonth() + 1)).slice(-2);
    return str;
};

function getCurMonth() {
    var mydate = new Date();
    return ("0" + (mydate.getMonth() + 1)).slice(-2);
};

function getYear() {
    var mydate = new Date();
    return mydate.getFullYear();
};

function getCurrentMonthDay() {
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    return new Date(year, month, 0).getDate();
}

function getMonthDay(year, month) {
    return new Date(year, month, 0).getDate();
}

// 计算指定时间是星期几
function getweekday(date) {
    // date例如:'2022-03-05'
    var weekArray = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
    var week = weekArray[new Date(date).getDay()]
    return week
}


function getPreMonth(yearMonth) {
    var arr = yearMonth.split("-");
    var year = arr[0]; //获取当前日期的年份
    var month = arr[1]; //获取当前日期的月份

    var year2 = year;
    var month2 = parseInt(month) - 1;
    if (month2 == 0) {
        //1月的上一月是前一年的12月
        year2 = parseInt(year2) - 1;
        month2 = 12;
    }

    if (month2 < 10) {
        //10月之前都需要补0
        month2 = "0" + month2;
    }
    var preMonth = year2 + "-" + month2;
    return preMonth;
}


function getNextMonth(yearMonth) {
    var arr = yearMonth.split("-");
    var year = arr[0]; //获取当前日期的年份
    var month = arr[1]; //获取当前日期的月份
    var day = arr[2]; //获取当前日期的日

    var year2 = year;
    var month2 = parseInt(month) + 1;
    if (month2 == 13) {
        //12月的下月是下年的1月
        year2 = parseInt(year2) + 1;
        month2 = 1;
    }
    if (month2 < 10) {
        //10月之前都需要补0
        month2 = "0" + month2;
    }

    var nextMonth = year2 + "-" + month2;
    return nextMonth;
}

// true:数值型的，false：非数值型
function myIsNaN(value) {
    return (typeof value === 'number' && !isNaN(value));
}

/**
 * 校验是否包含小数
 * @param numVal
 * @returns {boolean}
 */
function isDotNum(numVal) {
    var reg = /^\d+(?=\.{0,1}\d+$|$)/;
    if (!reg.test(numVal)) {
        // 返回，不往下执行
        return false;
    }
    return true;
}

function color16() {//十六进制颜色随机
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    const color = `#${r.toString(16)}${g.toString(16)}${b.toString(16)}`;
    return color;
}


// ----------------------------查询工具栏--------------------------------------------------------------

function checkInput(_this) {
    if (_this.value != '' && _this.value.substr(0, 1) == '.') {
        _this.value = '0.00';
    }
    if (_this.value == '') {
        _this.value = '';
        return;
    }
    _this.value = _this.value.replace(/^0*(0\.|[1-9])/, '$1'); // 禁止粘贴
    _this.value = _this.value.replace(/[^\d.]/g, ''); // 禁止输入非数字
    _this.value = _this.value.replace(/\.{2,}/g, '.'); // 只保留第一个. 清除多余的
    _this.value = _this.value.replace('.', '$#$').replace(/\./g, '').replace('$#$', '.');
    _this.value = _this.value.replace(/^(\-)*(\d+)\.(\d\d).*$/, '$1$2.$3'); // 只能输入两个小数

    if (_this.value.indexOf('.') < 0 && _this.value != '') {
        // 以上已经过滤，此处控制的是如果没有小数点，首位不能为类似于 01、02的金额
        if (_this.value.substr(0, 1) == '0' && _this.value.length == 2) {
            _this.value = _this.value.substr(1, _this.value.length);
        }
    }
    if (!_this.value) {
        _this.value = 0.0;
    }
}

function checkNum(_this) {
    // 失去焦点的时候判断 如果最后一位是 . 末尾补0
    if (_this.value == '') {
        _this.value = '';
    } else if (_this.value.indexOf('.') != -1) {
        if (_this.value.endsWith('.')) {
            _this.value += '00';
        } else if (_this.value.charAt(_this.value.length - 2) == '.') {
            _this.value += '0';
        }
    } else {
        _this.value += '.00';
    }
}

function selectTag(id, options) {
    // options  {value:name, value:name}
    let html = '<select class="form-control input-sm" id="' + id + '">';

    for (let i = 0; i < options.length; i++) {
        html += '<option value="' + options[i].key + '"';
        if (options[i].selected) {
            html += 'selected="selected"';
        }
        html += ' >' + options[i].value + '</option>';
    }
    return html + '</select>';
}

function queryToolbarFooter(obj) {
    let html = '<div class="querytoolbar-footer">'
        + '<div>'
    let queryFooter = '<div class="col-xs-offset-5">';
    for (let i = 0; i < obj.length; i++) {
        if ('button'.localeCompare(obj[i].tag) == 0) {
            queryFooter += '<button class="btn btn-primary btn-xs" id="' + obj[i].id + '">' + obj[i].desc + '</button> &nbsp;';
        }
    }
    html += queryFooter;
    // html += '</div><div class="clearfix"></div>';
    html += '</div></div>';
    return html;
}


// ----------------------------弹框录入--------------------------------------------------------------

function dialogPopove(title, bodyobj, linebreak) {
    let html = '<div class="white_content"  id="popoveModal" tabindex="-1" role="dialog" aria-labelledby="popoveModal">'
    html += '<div id="popoveModalDialog" class="modal-dialog" role="document">'
    html += '<div class="modal-content">';
    html += dialogPopoveHeader(title);
    html += dialogPopoveBody(bodyobj, linebreak);
    html += dialogPopoveFooter();
    html += "</div></div></div>";

    return html;
}

function dialogPopoveHeader(title) {
    return '<div class="modal-header">'
        + '<div class="col-sm-offset-1 col-sm-2">'
        + '<span id="title">' + title + '</span>'
        + '</div>'
        + '<div class="col-sm-offset-8 col-sm-1">'
        + '<a href="javascript:void(0)" id="close">'
        + '<i class="glyphicon glyphicon-remove"></i>'
        + '</a>'
        + '</div>'
        + '</div>';
}

function dialogPopoveBody(obj, linebreak) {
    let html = '<div class="modal-body">'
        + '<form class="form-horizontal" role="form">'
        + '<div class="row">'
        + '<div class="col-xs-12">';

    // html += formGroup(obj, linebreak);

    html += "</div></div></form></div>";
    return html;
}

function dialogPopoveFooter() {
    return '<div class="modal-footer"> \
        <div id ="poptips" style="float:left;color:red;"></div> \
        <button type="submit" class="btn btn-primary  btn-xs" id="sure">确定</button> \
        <input type="button" class= \'btn btn-primary btn-xs\' value="取消" id="cancel"/> \
        </div>';
}

function initpopoveModalDialog($element, title, dialogbodyObj, linebreak, url) {
    $element.append(dialogPopove(title, dialogbodyObj, linebreak));

    $("#popoveModalDialog").draggable();//为模态对话框添加拖拽
    $("#popoveModal").css("overflow", "hidden");//禁止模态对话框的半透明背景滚动

    $("#dbSelectModalDialog").draggable();//为模态对话框添加拖拽
    $("#dbSelectModal").css("overflow", "hidden");//禁止模态对话框的半透明背景滚动

    $("#fileImportModalDialog").draggable();//为模态对话框添加拖拽
    $("#fileImportModal").css("overflow", "auto");//禁止模态对话框的半透明背景滚动

    // 绑定弹框事件
    $('#cancel').click(function () {
        $('#popoveModal').css({display: 'none'});
        $('#fade').css({display: 'none'});
        for (let i = 0; i < dialogbodyObj.length; i++) {
            $('#' + dialogbodyObj[i].id).val("");
        }
        ;
    });


    $('#close').click(function () {
        $('#popoveModal').css({display: 'none'});
        $('#fade').css({display: 'none'});
        for (let i = 0; i < dialogbodyObj.length; i++) {
            $('#' + dialogbodyObj[i].id).val("");
        }
        ;
    });

    // 确定按钮

    $('#sure').click(function () {
        let data = {}
        let requireTips = [];

        for (let i = 0; i < dialogbodyObj.length; i++) {
            let value = $('#' + dialogbodyObj[i].id).val();
            if (dialogbodyObj[i].require) {
                if (value) {
                    data[dialogbodyObj[i].id] = value;
                } else {
                    requireTips.push(dialogbodyObj[i].label);
                }
            } else {
                data[dialogbodyObj[i].id] = value;
            }
        }
        if (requireTips.length > 0) {
            let tips = "必填："
            for (let i = 0; i < requireTips.length; i++) {
                tips = tips + requireTips[i] + "/";
            }
            $('#poptips').text(tips);

            return;
        }
        $('#poptips').text("");
        data["creatorcode"] = '1';
        data["createtime"] = getDate();

        $.ajax({
            url: url,
            type: 'post',
            data: data,
            // 上面data为提交数据，下面data形参指代的就是异步提交的返回结果data
            success: function (obj) {
                data = JSON.parse(obj);
                if ("1".localeCompare(data['code']) == 0) {
                    $('#popoveModal').css({display: 'none'});
                    $('#fade').css({display: 'none'});
                    for (let i = 0; i < dialogbodyObj.length; i++) {
                        $('#' + dialogbodyObj[i].id).val("");
                    }
                    ;
                    $("#table").bootstrapTable('refreshOptions', {pageNumber: 1,});
                    notices(data['msg']);
                } else {
                    $('#poptips').text(data['msg']);
                }
            },
            error: function (obj) {
                $('#poptips').text(obj);
            }
        });
    });
}

$('.selectpicker').datetimepicker()
    .on('changeDate', function (event) {
        event.preventDefault();
        event.stopPropagation();
        $('#id_disableTime').datetimepicker('setStartDate', event.date);
    });

$('.selectpicker').datetimepicker()
    .on('changeDate', function (event) {
        event.preventDefault();
        event.stopPropagation();
        $("#id_enableTime").datetimepicker('setEndDate', event.date);
    });

$('.selectpicker').datetimepicker()