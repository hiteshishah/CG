//
// Vertex shader for the transformation assignment
//
// Created by Warren R. Carithers 2016/04/22.
//
// Contributor:  Hiteshi Shah
//

#version 150

// attribute:  vertex position
in vec4 vPosition;

uniform float currentProjection;

float left = -1.0,
	  right = 1.0,
	  top = 1.0,
	  bottom = -1.0,
	  near = 0.9,
	  far = 4.5;

uniform vec3 ey;
uniform vec3 la;
uniform vec3 up;

uniform vec3 sc;
uniform vec3 ro;
uniform vec3 tr;

void setFrustum(out mat4 projection) {
	projection = mat4((2 * near) / (right - left), 0, 0, 0,
		0, (2 * near) / (top - bottom), 0, 0,
		(right + left) / (right - left), (top + bottom) / (top - bottom), -(far + near) / (far - near), -1,
		0, 0, (-2 * far * near) / (far - near), 0);
}

void setOrtho(out mat4 projection) {
	projection = mat4(2 / (right - left), 0, 0, 0,
		0, 2 / (top - bottom), 0, 0,
		0, 0, -2 / (far - near), 0,
		-(right + left) / (right - left), -(top + bottom) / (top - bottom), -(far + near) / (far - near), 1);
}

void setView(out mat4 view) {
	vec3 n = normalize(ey - la);
	vec3 u = normalize(cross(up, n));
	vec3 v = normalize(cross(n, u));

	float du = -1.0 * dot(u, ey);
	float dv = -1.0 * dot(v, ey);
	float dn = -1.0 * dot(n, ey);

	view = mat4(u.x, v.x, n.x, 0.0,
		u.y, v.y, n.y, 0.0,
		u.z, v.z, n.z, 0.0,
		du, dv, dn, 1.0);
}

void scale(out mat4 s) {
	s = mat4(sc.x, 0.0, 0.0, 0.0,
		0.0, sc.y, 0.0, 0.0,
		0.0, 0.0, sc.z, 0.0,
		0.0, 0.0, 0.0, 1.0);
}

void rotate(out mat4 r) {
	vec3 angle = radians(ro),
		cos = cos(angle),
		sin = sin(angle);

	mat4 x = mat4(1.0, 0.0, 0.0, 0.0,
		0.0, cos.x, sin.x, 0.0,
		0.0, -sin.x, cos.x, 0.0,
		0.0, 0.0, 0.0, 1.0);

	mat4 y = mat4(cos.y, 0.0, -sin.y, 0.0,
		0.0, 1.0, 0.0, 0.0,
		sin.y, 0.0, cos.y, 0.0,
		0.0, 0.0, 0.0, 1.0);

	mat4 z = mat4(cos.z, sin.z, 0.0, 0.0,
		-sin.z, cos.z, 0.0, 0.0,
		0.0, 0.0, 1.0, 0.0,
		0.0, 0.0, 0.0, 1.0);

	r = z * y * x;
}

void translate(out mat4 t) {
	t = mat4(1.0, 0.0, 0.0, tr.x,
		0.0, 1.0, 0.0, tr.y,
		0.0, 0.0, 1.0, tr.z,
		0.0, 0.0, 0.0, 1.0);
}

void main()
{
    mat4 projection, view;
	mat4 s, r, t;

	if (currentProjection == 1) {
		setFrustum(projection);
	}
	else {
		setOrtho(projection);
	}

	setView(view);

	scale(s);
	rotate(r);
	translate(t);

    gl_Position = projection * view * s * r * t * vPosition;

}
