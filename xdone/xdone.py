import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, Boolean
from xblock.fragment import Fragment


class XDoneXBlock(XBlock):

    """

    Button to set mark a current section as passed.

    """

    done = Boolean(
        default=False, scope=Scope.user_state,
        help="The mark a student finished task"
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the XDoneXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/xdone.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/xdone.css"))
        frag.add_javascript(self.resource_string("static/js/src/xdone.js"))
        frag.initialize_js('XDoneXBlock')
        return frag

    @XBlock.json_handler
    def done_submit(self, data, suffix=''):
        """
        handler, mark section as done
        """

        self.done = True
        return {"done": self.done}


    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("XDoneXBlock",
             """<xdone/>
             """),
            ("Multiple XDoneXBlock",
             """<vertical_demo>
                <xdone/>
                <xdone/>
                <xdone/>
                </vertical_demo>
             """),
        ]
