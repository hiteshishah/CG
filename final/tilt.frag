#version 150

// tilt fragment shader
//
// Contributor:  Hiteshi Shah

// INCOMING DATA

// Material properties of the teapot and quad
uniform vec4 tilt_ambient_material_color;
uniform float tilt_ambient_reflection_coefficient;
uniform vec4 tilt_diffuse_material_color;
uniform float tilt_diffuse_reflection_coefficient;
uniform vec4 tilt_specular_material_color;
uniform float tilt_specular_exponent;
uniform float tilt_specular_reflection_coefficient;

// Properties of the light source
uniform vec4 tilt_light_color;

// Properties of the ambient light
uniform vec4 tilt_ambient_light;

in vec3 vNorm;
in vec3 light;
in vec3 vPos;

void main()
{
	vec3 N = normalize(vNorm);
	vec3 L = normalize(light - vPos);
	vec3 R = normalize (reflect(-L, N));
    vec3 V = normalize (-vPos);

	// ambient
	vec4 ambient = tilt_ambient_material_color * tilt_ambient_reflection_coefficient * tilt_ambient_light;

	// diffuse
	vec4 diffuse = tilt_diffuse_material_color * tilt_diffuse_reflection_coefficient * (dot(L, N));

	// specular
	vec4 specular = tilt_specular_material_color * tilt_specular_reflection_coefficient * pow(max(0.0, dot(R, V)), tilt_specular_exponent);

	gl_FragColor = ambient + tilt_light_color * (diffuse + specular);
}
