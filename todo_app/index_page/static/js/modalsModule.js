var modalsModule = (function() {

  return {
    renderOverlay: function(){
      var overlayEl = $(`
        <div class="modal-overlay__element">

        </div>
      `);
      $('body').append(overlayEl);
      overlayEl.animate({
        opacity: '1'
      }, 300);
    },
    hideOverlay: function(){
      $('.modal-overlay__element').animate({
        opacity: '0'
      }, 300).remove();
    },
    openModal: function(el, delay){
      this.renderOverlay();
      el.show().animate({
        'top': '100px'
      }, delay);
    },
    closeModal: function(el, delay){
      this.hideOverlay();
      el.animate({
        'top': '100vh'
      }, delay).hide(delay);
    }


  }
}());
