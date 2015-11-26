var sth=$;
var vote_util={
    count:2,
    optionHTML:'<a id="option<%=i%>" href="#" class="list-group-item">'+
        '<div id="datetime<%=i%>" class="input-group date form_datetime">'+
              '<span class="input-group-addon"><%=i%>.</span>'+
              '<input class="form-control" size="10" type="text" value="" readonly>'+
              '<span class="option-delete input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>'+
			  '<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>'+
        '</div>'+'</a>',
    bind_group:function(){
        $(".groupselect").click(function(e){
            var $select=$(e.target).closest(".groupselect");
            var groupid=$select.attr("data-groupid");
            var groupname=$select.attr("data-groupname");
            $("a#selectedgroup").html(groupname+'<b class="caret"></b>')
            selected_data.groupid=groupid;
            // TODO
            console.log(groupname);
        });
    },
    del_option:function(){
    },
    bind:function(){
        $=sth;
        vote_util.bind_group();
        var add_option=function(){
            var i=vote_util.count;
            vote_util.count++;
            var html=_.template(vote_util.optionHTML)({
                i:i
            });
            $("div#optionlist").append(html);
            $("a#option"+i+" span.option-delete").on("click",function(e){
                $(e.target).closest("a").remove();
            });
            $("a#option"+i+" .form_datetime").datetimepicker({
                weekStart: 1,
                format: 'yyyy-mm-dd hh:ii',
                todayBtn:  1,
		        autoclose: 1,
		        todayHighlight: 1,
		        startView: 2,
		        forceParse: 0,
                showMeridian: 1
            });
        };
        $("button#addoption").click(function(){
            add_option();
        });
    },
    add_vote_submit:function(){
        var form={
            votetitle:$("input#votetitle").val(),
            votelimit:$("input#votelimit").val(),
            votegroupid:selected_data.groupid,
            voteoption:vote_util.get_options()
        };
    },
    get_options:function(){
        var $datetime=$('.form_datetime');
        var dates=[];
        for(var i=0;i<$datetime.length;i++){
            var picker=$($datetime[i]).datetimepicker();
            var date=picker.data().date;
            if(date){
                dates.push(date+":00");
            }
        }
        return dates;
    }
}
$(document).ready(function(){
    vote_util.bind();
});
