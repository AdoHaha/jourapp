// Generated by CoffeeScript 1.6.1
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
    _this = this;

  window.App = window.App || {};

  App.AllWords = (function(_super) {

    __extends(AllWords, _super);

    function AllWords() {
      return AllWords.__super__.constructor.apply(this, arguments);
    }

    AllWords.prototype.urlRoot = "/journals";

    AllWords.prototype.noofwords = 0;

    return AllWords;

  })(Backbone.Model);

  App.JournalForm = (function(_super) {

    __extends(JournalForm, _super);

    function JournalForm() {
      var _this = this;
      this.countandsave = function() {
        return JournalForm.prototype.countandsave.apply(_this, arguments);
      };
      this.count = function() {
        return JournalForm.prototype.count.apply(_this, arguments);
      };
      this.keypressed = function(event) {
        return JournalForm.prototype.keypressed.apply(_this, arguments);
      };
      this.skonczyl = function() {
        return JournalForm.prototype.skonczyl.apply(_this, arguments);
      };
      this.autosave = function() {
        return JournalForm.prototype.autosave.apply(_this, arguments);
      };
      this.synchstring = function() {
        return JournalForm.prototype.synchstring.apply(_this, arguments);
      };
      this.probablyendend = function() {
        return JournalForm.prototype.probablyendend.apply(_this, arguments);
      };
      this.journalchanged = function() {
        return JournalForm.prototype.journalchanged.apply(_this, arguments);
      };
      return JournalForm.__super__.constructor.apply(this, arguments);
    }

    JournalForm.prototype.el = $("#journal_form");

    JournalForm.prototype.initialize = function() {
      $("#journaltext").autosize();
      $('#journaltext').trigger('autosize.resize');
      $('#journaltext').autosize({
        append: "\n"
      });
      this.autosavenr = this.model.get("noofwords");
      setTimeout(this.autosave, 7000);
      this.sthchanged = false;
      this.model.on({
        change: this.journalchanged
      });
      this.model.on({
        sync: this.synchstring
      });
      this.maintext = $("#journaltext");
      $('#journaltext').focus();
      App.moveCursorToEnd(document.getElementById("journaltext"));
      $("#journaltext").tabby({
        tabString: '        '
      });
      this.count();
      this.currtime = new Date();
      return this;
    };

    JournalForm.prototype.events = {
      "focusout #journaltext": "probablyendend",
      "blur #journaltext": "probablyendend",
      "keypress #journaltext": "keypressed",
      "focus window": "autosave"
    };

    JournalForm.prototype.journalchanged = function() {
      console.log("journal changed triggered");
      $("#journaltext").val(this.model.get("allwords"));
      $("#journaltext").trigger('autosize.resize');
      return this;
    };

    JournalForm.prototype.probablyendend = function() {
      this.sthchanged = true;
      return this.countandsave;
    };

    JournalForm.prototype.synchstring = function() {
      var updatestring;
      updatestring = "Synced " + this.model.get("noofwords") + " at " + this.currtime.getHours() + ":" + this.currtime.getMinutes();
      $("#save_message").text(updatestring);
      return this;
    };

    JournalForm.prototype.autosave = function() {
      setTimeout(this.autosave, 7000);
      if (!this.sthchanged) {
        this.model.fetch();
      } else {
        this.countandsave();
        this.autosavenr = this.model.get("noofwords");
        $("#autosaving_indication").removeClass("not-saved").addClass("saved");
        this.sthchanged = false;
      }
      return this;
    };

    JournalForm.prototype.skonczyl = function() {
      this.model.set({
        "allwords": $("#journaltext").text()
      });
      return this.countwords();
    };

    JournalForm.prototype.keypressed = function(event) {
      this.sthchanged = true;
      if (event.which === 32 || event.which === 13 || event.which === 8) {
        this.count();
      }
      return this;
    };

    JournalForm.prototype.count = function() {
      var noofwords, result, words, words2;
      words = $("#journaltext").val();
      words2 = words;
      words2.replace(/(^\s*)|(\s*$)/gi, "");
      words2.replace(/[ ]{2,}/gi, " ");
      words2.replace(/\n /, "\n");
      noofwords = words2.split(' ').length;
      if (noofwords > 0) {
        $(this.el).find('textarea').css({
          "border": "0"
        });
      }
      $(".count").text(noofwords + " " + "words");
      result = {
        allwords: words,
        noofwords: noofwords
      };
      if (this.autosavenr !== noofwords) {
        $("#autosaving_indication").removeClass("saved").addClass("not-saved");
      }
      this.backgroundmotivator(noofwords);
      if (noofwords >= 750 && !App.jetOver750) {
        $("#result").removeClass("hidden").addClass("alert alert-success");
        $("#result").append("You have successfully written over 750 words today! Congrats x 1000! Keep up the good work");
        $("#result").alert();
        App.jetOver750 = true;
      }
      return result;
    };

    JournalForm.prototype.backgroundmotivator = function(noofwords) {
      var prop;
      if (noofwords <= 750) {
        prop = Math.floor(255 * (noofwords / 750));
        $("body").css("background-color", "rgb(255," + prop + "," + prop + ")");
      } else {
        $("body").css("background-color", "#ffffff");
      }
      return this;
    };

    JournalForm.prototype.countandsave = function() {
      var result;
      result = this.count();
      this.model.set(result);
      this.model.save();
      return this;
    };

    return JournalForm;

  })(Backbone.View);

  App.moveCursorToEnd = function(el) {
    var range;
    if (typeof el.selectionStart === "number") {
      return el.selectionStart = el.selectionEnd = el.value.length;
    } else if (typeof el.createTextRange !== "undefined") {
      el.focus();
      range = el.createTextRange();
      range.collapse(false);
      return range.select();
    }
  };

}).call(this);
