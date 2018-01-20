const showLoading = isLoading => isLoading && <Loader />;

const showError = status =>
  status.message && status.type ? <Text>{status.message}</Text> : null;

function charlie() {
	console.log("test");

	return () => {}
}

function testMe(){
	return {
		test: () => {},
		test2: function charlie(hej) {

		}
	}
}

(function(){

})()

let test=function(){

}

const testing = function() {

}

let test = () => {

}

let test = function testMe() {

}

const LoginPage = ({ loginWithFacebook, loginWithGmail, isLoading, status }) =>
  showLoading(isLoading.action) || (
    <View style={pageStyle}>
      <View style={headerStyle}>
        <Text style={titleStyle}>Don't break the chain</Text>
        <Text style={sloganStyle}>Every new habit starts with a goal</Text>
        {process.env.REACT_APP_MODE !== "production" && (
          <Text
			onClick={() => console.log("Charlie")}
			onHej={testing => console.log()}
			hejsan={function() {

			}}
            style={{
              display: "block",
              color: colors.lightGrey,
              fontSize: "10px",
              position: "absolute",
              top: "10px",
              right: "10px"
            }}
          >
            (Beta version)
          </Text>
        )}
      </View>
      <View style={contentStyle}>
        {showError(status)}

        <img src={CalendarImage} alt="" style={imageStyle} />

        <RaisedButton handleClick={loginWithFacebook} customStyle={buttonStyle}>
          <Text style={{ color: colors.white }}>Login with Facebook</Text>
        </RaisedButton>

        <RaisedButton handleClick={loginWithGmail} customStyle={buttonStyle}>
          <Text style={{ color: colors.white }}>Login with Gmail</Text>
        </RaisedButton>

        <a
          href="https://www.writersstore.com/dont-break-the-chain-jerry-seinfeld/"
          target="__blank"
        >
          <Text style={{ fontSize: "10px" }}>What is this?</Text>
        </a>
      </View>
    </View>
  );

const withLogin = compose(
  connect(getAuth, { loginWithFacebook, loginWithGmail }),
  lifecycle({
    componentDidMount() {
      return this.props.user
        ? this.props.history.replace(
            this.props.location.search.replace("?next=", "")
          )
        : null;
    },
    componentDidUpdate() {
      return this.props.user
        ? this.props.history.replace(
            this.props.location.search.replace("?next=", "")
          )
        : null;
    }
  })
);

export default withLogin(LoginPage);
