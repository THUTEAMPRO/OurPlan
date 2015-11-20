var group_util={
    listTemplateHTML:'<li><label data-groupid="<%=groupid%>" data-groupname="<%=groupname%>">'+
        '<input class="groupselect" name="groupselect" type="radio"/>'+
        '<%=groupname%>'+
        '</label></li>',
    bind:function(){
        $("ul#group").html("");
        for(var i=0;i<group_data.length;i++){
            var groupname=group_data[i].groupname;
            var listHTML=_.template(group_util.listTemplateHTML)({
                groupname:group_data[i].groupname,
                groupid:group_data[i].groupid
            });
            $("ul#group").append(listHTML);
        }
        $("button#addgroup").on("click",function(){
            var groupname=$("#groupname").val();
            $.post("/api/add_group", {
                groupname:groupname
            },
                   function(data){
                       if(data.fail){
                           alert("update fail");
                       }else{
                           var listHTML=_.template(group_util.listTemplateHTML)({
                               groupname:groupname,
                               groupid:data.id
                           });
                           $("ul#group").append(listHTML);
                       }
                   });
        });
        $("ul#group").click(function(e){
            var $input=$(e.target).closest("input[name=groupselect]");
            if($input.length==1){
                var $label=$input.closest("label");
                var groupname=$label.attr("data-groupname")
                console.log(groupname);
            }
        });
    }
}
$(document).ready(function(){
    group_util.bind();
});