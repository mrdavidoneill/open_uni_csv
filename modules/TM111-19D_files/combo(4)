/**
 * YUI3 local Annotate initiation.
 */
YUI.add('moodle-local_annotate-alwayson', function(Y){
    M.local_annotate = {
        init: function(params){
            if (document.getElementById('ouannotate-disable')) {
                return; // Do not add alwayson to annotate disabled pages.
            }
            var s = document.createElement('script');
            s.id = 'ou_a_b';
            s.src = params.bootstrap;
            document.body.appendChild(s);
            var d = document.createElement('div');
            d.id = 'ou_a_bb';
            document.body.appendChild(d);
        }
    };
}, '@VERSION@', {
    requires: ['base']
});