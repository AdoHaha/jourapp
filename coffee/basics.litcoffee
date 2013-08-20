All the goodness to make journaling motivating
=======================================

        window.App = window.App||{};

King of this program, form view.
It counts all and shows shit
        class App.AllWords extends Backbone.Model
                urlRoot: "/journals"
                noofwords: 0        
        class App.JournalForm extends Backbone.View
                el:$("#journal_form")
                initialize: ->
                        $("#journaltext").autosize();
                        $('#journaltext').trigger('autosize.resize')      
                        $('#journaltext').autosize({append: "\n"})
                        @autosavenr=@model.get("noofwords")
                        setTimeout(@autosave,7000) #every 7 sec
                        @sthchanged=false #we keep state of freshness, in case user opened two windows - it will update older state
                        @model.on({change:@journalchanged})
                        @model.on({sync:@synchstring})
                        @maintext=$("#journaltext")
                        $('#journaltext').focus();
                        App.moveCursorToEnd(document.getElementById("journaltext"))
                        
                        $("#journaltext").tabby({tabString:'        '})
                        @count()
                        @currtime=new Date()
                        @
Model will be saved when focus is out or just new word entered. 

                events:
                        
                        "focusout #journaltext":"probablyendend"
                        "blur #journaltext":"probablyendend"
                        "keypress #journaltext": "keypressed"
                        "focus window": "autosave"
                journalchanged: =>
                        #console.log("journal changed triggered")
                        $("#journaltext").text(@model.get("allwords"))
                        $("#journaltext").trigger('autosize.resize')
                        @
                        
                probablyendend: =>
                        @sthchanged=true
                        @countandsave
                synchstring: =>
                        updatestring="Synced "+@model.get("noofwords")+ " at " +@currtime.getHours()+":"+ @currtime.getMinutes()
                        $("#save_message").text(updatestring)
                        @
                autosave: =>
                        
                        setTimeout(@autosave,7000)
                        if not @sthchanged
                                @model.fetch()
                                #console.log("will only fetch")
                        else
                                @countandsave()
                              
                                
                                @autosavenr=@model.get("noofwords")
                                $("#autosaving_indication").removeClass("not-saved").addClass("saved")
                                   
                                @sthchanged=false
                        
                        @
                skonczyl: =>
                        @model.set({"allwords":$("#journaltext").text()})
                        
                        @countwords()
                        
If enter, space or backspace is pressed, counting will be updated
                keypressed: (event) =>
                        @sthchanged=true
                        if (event.which ==32 || event.which==13 || event.which==8)
                                
                                @count()
                        @
                        
                count: =>
                        words=$("#journaltext").val()
                        words2=words
                        words2.replace(/(^\s*)|(\s*$)/gi,"");
                        words2.replace(/[ ]{2,}/gi," ");
                        words2.replace(/\n /,"\n");
                        noofwords=words2.split(' ').length
                        #show
                        if noofwords>0
                                $(@el).find('textarea').css({"border": "0"})
                        $(".count").text(noofwords+" "+"words")
                        result={allwords:words,noofwords:noofwords}
                        #console.log(result)
                        if @autosavenr!=noofwords
                                $("#autosaving_indication").removeClass("saved").addClass("not-saved")
                                
                        @backgroundmotivator(noofwords)        
                        if noofwords>=750 and not App.jetOver750
                                #show success alert
                                $("#result").removeClass("hidden").addClass("alert alert-success")
                                $("#result").append("You have successfully written over 750 words today! Congrats x 1000! Keep up the good work")
                                $("#result").alert()
                                App.jetOver750=true
                        result
                backgroundmotivator: (noofwords)->
                        if noofwords<=750
                             prop=Math.floor(255*(noofwords/750))
                             $("body").css("background-color","rgb(255,"+(prop)+","+(prop)+")") 
                        else
                             $("body").css("background-color","#ffffff")
                             
                        @  
                countandsave: =>
                        
                        #count
                        result=@count()
                       #save  
                        #console.log(result)
                        @model.set(result)  
                        @model.save()
                        @
                       
                
                
Little helper function, to set the focus right
        App.moveCursorToEnd = (el) ->
                if (typeof el.selectionStart == "number") 
                        el.selectionStart = el.selectionEnd = el.value.length;
                else if (typeof el.createTextRange != "undefined")
                        el.focus();
                        range = el.createTextRange();
                        range.collapse(false);
                        range.select();
    
 
                
                
                
                


      
